from flask import Blueprint, render_template, request, redirect, url_for, flash, session, send_file, jsonify
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import io
from models import db, User, Complaint
from werkzeug.utils import secure_filename
from config import Config, PROJECT_ROOT
import os
from datetime import datetime

user_bp = Blueprint('user', __name__)

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        
        # Validation
        if not name or not email or not password:
            flash('All fields are required!', 'danger')
            return redirect(url_for('user.register'))
        
        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('user.register'))
        
        if len(password) < 6:
            flash('Password must be at least 6 characters!', 'danger')
            return redirect(url_for('user.register'))
        
        # Check if user exists
        if User.query.filter_by(email=email).first():
            flash('Email already registered!', 'danger')
            return redirect(url_for('user.register'))
        
        # Create new user
        user = User(name=name, email=email)
        user.set_password(password)
        
        try:
            db.session.add(user)
            db.session.commit()
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('user.login'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred during registration!', 'danger')
            return redirect(url_for('user.register'))
    
    return render_template('register.html')

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        
        if not email or not password:
            flash('Email and password are required!', 'danger')
            return redirect(url_for('user.login'))
        
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['user_name'] = user.name
            session['is_admin'] = user.is_admin
            session.permanent = True
            
            if user.is_admin:
                flash(f'Welcome Admin {user.name}!', 'success')
                return redirect(url_for('admin.dashboard'))
            else:
                flash(f'Welcome {user.name}!', 'success')
                return redirect(url_for('user.view_complaints'))
        else:
            flash('Invalid email or password!', 'danger')
            return redirect(url_for('user.login'))
    
    return render_template('login.html')

@user_bp.route('/logout')
def logout():
    """User logout"""
    session.clear()
    flash('You have been logged out!', 'info')
    return redirect(url_for('index'))

def login_required(f):
    """Decorator to check if user is logged in"""
    from functools import wraps
    
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login first!', 'warning')
            return redirect(url_for('user.login'))
        return f(*args, **kwargs)
    return decorated_function

@user_bp.route('/submit-complaint', methods=['GET', 'POST'])
@login_required
def submit_complaint():
    """Submit a new complaint"""
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        location = request.form.get('location', '').strip()
        
        # Validation
        if not title or not description or not location:
            flash('All fields are required!', 'danger')
            return redirect(url_for('user.submit_complaint'))
        
        image_path = None
        
        # Handle file upload
        if 'image' in request.files:
            file = request.files['image']
            if file and file.filename and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                # Add timestamp to filename to make it unique
                filename = f"{datetime.utcnow().timestamp()}_{filename}"
                # Ensure absolute path for upload folder
                upload_folder = Config.UPLOAD_FOLDER
                if not os.path.isabs(upload_folder):
                    upload_folder = os.path.join(PROJECT_ROOT, 'static/uploads')
                os.makedirs(upload_folder, exist_ok=True)
                filepath = os.path.join(upload_folder, filename)
                file.save(filepath)
                image_path = filename  # Store only filename, not full path
            elif file and file.filename:
                flash('Invalid file type! Only PNG, JPG, JPEG, GIF are allowed.', 'danger')
                return redirect(url_for('user.submit_complaint'))
        
        # Create complaint
        complaint = Complaint(
            user_id=session['user_id'],
            title=title,
            description=description,
            location=location,
            image_path=image_path,
            status='Pending'
        )
        
        try:
            db.session.add(complaint)
            db.session.commit()
            flash('Complaint submitted successfully!', 'success')
            return redirect(url_for('user.view_complaints'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred while submitting complaint!', 'danger')
            return redirect(url_for('user.submit_complaint'))
    
    return render_template('complaint_form.html')

@user_bp.route('/view-complaints')
@login_required
def view_complaints():
    """View user's complaints"""
    page = request.args.get('page', 1, type=int)
    complaints = Complaint.query.filter_by(user_id=session['user_id']).order_by(
        Complaint.created_at.desc()
    ).paginate(page=page, per_page=10)
    
    return render_template('user_dashboard.html', complaints=complaints)

@user_bp.route('/complaint/<int:complaint_id>')
@login_required
def view_complaint_detail(complaint_id):
    """View complaint details with comparison data"""
    complaint = Complaint.query.get_or_404(complaint_id)
    
    # Check if user owns this complaint
    if complaint.user_id != session['user_id'] and not session.get('is_admin'):
        flash('You do not have permission to view this complaint!', 'danger')
        return redirect(url_for('user.view_complaints'))
    
    # Feature 3: Resolution time
    resolution_days = None
    if complaint.status == 'Resolved' and complaint.updated_at:
        resolution_days = (complaint.updated_at - complaint.created_at).days
    
    # Feature 4: Area impact - complaints count before/after this complaint
    before_count = db.session.query(db.func.count(Complaint.id)).filter(
        Complaint.location == complaint.location,
        Complaint.created_at < complaint.created_at
    ).scalar() or 0
    
    after_count = db.session.query(db.func.count(Complaint.id)).filter(
        Complaint.location == complaint.location,
        Complaint.created_at >= complaint.created_at
    ).scalar() or 0
    
    # Feature 2: Previous status (simple: always starts as Pending/Reported)
    previous_status = 'Reported'
    
    return render_template('complaint_detail.html', 
                         complaint=complaint,
                         resolution_days=resolution_days,
                         before_count=before_count,
                         after_count=after_count,
                         previous_status=previous_status)


@user_bp.route('/map-data')
@login_required
def map_data():
    """Return user's complaints for map as JSON"""
    complaints = Complaint.query.filter_by(user_id=session['user_id']).all()
    data = []
    for c in complaints:
        if c.latitude and c.longitude:
            data.append({
                'title': c.title,
                'lat': float(c.latitude),
                'lng': float(c.longitude),
                'status': c.status
            })
    return jsonify(data)


@user_bp.route('/generate-pdf/<int:complaint_id>')
@login_required
def generate_pdf(complaint_id):
    """Generate downloadable PDF report for complaint"""
    complaint = Complaint.query.get_or_404(complaint_id)
    
    # Permission check - user must own complaint or be admin
    if complaint.user_id != session['user_id'] and not session.get('is_admin'):
        flash('You do not have permission to generate report for this complaint!', 'danger')
        return redirect(url_for('user.view_complaints'))
    
    # Create PDF in memory
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    
    story = []
    
    # Title
    title_style = styles['Title']
    title_style.alignment = 1  # Center
    story.append(Paragraph("Complaint Report", title_style))
    story.append(Spacer(1, 20))
    
    # Complaint details with bold labels
    normal_style = styles['Normal']
    bold_style = styles['Heading2']
    
    details = [
        ("Complaint ID:", f"#{complaint.id}"),
        ("Title:", complaint.title),
        ("Description:", complaint.description),
        ("Location:", complaint.location),
        ("Status:", complaint.status),
        ("Date:", complaint.created_at.strftime('%d %B %Y at %H:%M'))
    ]
    
    for label, value in details:
        story.append(Paragraph(f"<b>{label}</b>", bold_style))
        story.append(Paragraph(str(value), normal_style))
        story.append(Spacer(1, 12))
    
    # Horizontal separator line
    story.append(Paragraph("<hr width=100% height=2/>", normal_style))
    story.append(Spacer(1, 20))
    
    # Footer
    footer_style = styles['Italic']
    story.append(Paragraph("Generated by Citizen Feedback System", footer_style))
    
    # Build PDF
    doc.build(story)
    buffer.seek(0)
    
    return send_file(
        buffer,
        as_attachment=True,
        download_name=f"complaint_report_{complaint_id}.pdf",
        mimetype='application/pdf'
    )
