from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from models import db, User, Complaint
from functools import wraps
from datetime import datetime
from config import Config, PROJECT_ROOT
import os

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

def admin_required(f):
    """Decorator to check if user is admin"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login first!', 'warning')
            return redirect(url_for('user.login'))
        
        if not session.get('is_admin'):
            flash('You do not have permission to access this page!', 'danger')
            return redirect(url_for('index'))
        
        return f(*args, **kwargs)
    return decorated_function

@admin_bp.route('/dashboard')
@admin_required
def dashboard():
    """Admin dashboard with statistics"""
    total_complaints = Complaint.query.count()
    pending_complaints = Complaint.query.filter_by(status='Pending').count()
    in_progress_complaints = Complaint.query.filter_by(status='In Progress').count()
    resolved_complaints = Complaint.query.filter_by(status='Resolved').count()
    
    stats = {
        'total': total_complaints,
        'pending': pending_complaints,
        'in_progress': in_progress_complaints,
        'resolved': resolved_complaints
    }
    
    return render_template('admin_dashboard.html', stats=stats)

@admin_bp.route('/complaints')
@admin_required
def view_all_complaints():
    """View all complaints"""
    page = request.args.get('page', 1, type=int)
    status_filter = request.args.get('status', '', type=str)
    
    query = Complaint.query
    
    if status_filter and status_filter in ['Pending', 'In Progress', 'Resolved']:
        query = query.filter_by(status=status_filter)
    
    complaints = query.order_by(Complaint.created_at.desc()).paginate(page=page, per_page=15)
    
    return render_template('admin_complaints.html', complaints=complaints, status_filter=status_filter)

@admin_bp.route('/complaint/<int:complaint_id>/update-status', methods=['POST'])
@admin_required
def update_complaint_status(complaint_id):
    """Update complaint status and handle after_image upload"""
    complaint = Complaint.query.get_or_404(complaint_id)
    new_status = request.form.get('status', '').strip()
    
    if new_status not in ['Pending', 'In Progress', 'Resolved']:
        flash('Invalid status!', 'danger')
        return redirect(request.referrer or url_for('admin.view_all_complaints'))
    
    # Handle after_image upload for Resolved status
    if new_status == 'Resolved' and 'after_image' in request.files:
        file = request.files['after_image']
        if file and file.filename:
            from werkzeug.utils import secure_filename
            
            filename = secure_filename(file.filename)
            filename = f"{datetime.utcnow().timestamp()}_after_{filename}"
            # Ensure absolute path for upload folder
            upload_folder = Config.UPLOAD_FOLDER
            if not os.path.isabs(upload_folder):
                upload_folder = os.path.join(PROJECT_ROOT, 'static/uploads')
            os.makedirs(upload_folder, exist_ok=True)
            filepath = os.path.join(upload_folder, filename)
            file.save(filepath)
            complaint.after_image = filename  # Store only filename, not full path
    
    try:
        complaint.status = new_status
        complaint.updated_at = datetime.utcnow()  # Update timestamp
        db.session.commit()
        flash(f'Complaint status updated to {new_status}!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('An error occurred while updating status!', 'danger')
    
    return redirect(request.referrer or url_for('admin.view_all_complaints'))

@admin_bp.route('/complaint/<int:complaint_id>/delete', methods=['POST'])
@admin_required
def delete_complaint(complaint_id):
    """Delete a complaint"""
    complaint = Complaint.query.get_or_404(complaint_id)
    
    try:
        db.session.delete(complaint)
        db.session.commit()
        flash('Complaint deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('An error occurred while deleting complaint!', 'danger')
    
    return redirect(url_for('admin.view_all_complaints'))

@admin_bp.route('/statistics')
@admin_required
def statistics():
    """Detailed statistics page"""
    total_users = User.query.filter_by(is_admin=False).count()
    total_complaints = Complaint.query.count()
    pending = Complaint.query.filter_by(status='Pending').count()
    in_progress = Complaint.query.filter_by(status='In Progress').count()
    resolved = Complaint.query.filter_by(status='Resolved').count()
    
    # Get top locations with most complaints
    top_locations = db.session.query(
        Complaint.location,
        db.func.count(Complaint.id).label('count')
    ).group_by(Complaint.location).order_by(
        db.func.count(Complaint.id).desc()
    ).limit(10).all()
    
    stats = {
        'total_users': total_users,
        'total_complaints': total_complaints,
        'pending': pending,
        'in_progress': in_progress,
        'resolved': resolved,
        'top_locations': top_locations
    }
    
    return render_template('admin_statistics.html', stats=stats)

@admin_bp.route('/api_analytics')
@admin_required
def api_analytics():
    """JSON API for admin analytics chart data in dashboard"""
    top_locations = db.session.query(
        Complaint.location,
        db.func.count(Complaint.id).label('count')
    ).group_by(Complaint.location).order_by(
        db.func.count(Complaint.id).desc()
    ).limit(10).all()
    
    data = {
        'locations': [str(location) for location, count in top_locations],
        'counts': [int(count) for location, count in top_locations]
    }
    
    return jsonify(data)

