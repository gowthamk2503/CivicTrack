import os
from dotenv import load_dotenv
from flask import Flask, render_template, session, send_from_directory
from config import DevelopmentConfig, ProductionConfig, TestingConfig, Config, PROJECT_ROOT
from models import db, User, Complaint
from routes.user_routes import user_bp, login_required
from routes.admin_routes import admin_bp

load_dotenv()

def create_app(config_class=None):
    """Flask application factory"""
    if config_class is None:
        env = os.environ.get('FLASK_ENV', 'development').lower()
        if env == 'production':
            config_class = ProductionConfig
        elif env == 'testing':
            config_class = TestingConfig
        else:
            config_class = DevelopmentConfig

    template_dir = os.path.join(PROJECT_ROOT, 'templates')
    static_dir = os.path.join(PROJECT_ROOT, 'static')
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    app.config.from_object(config_class)
    
    # Ensure UPLOAD_FOLDER is an absolute path
    if not os.path.isabs(app.config['UPLOAD_FOLDER']):
        app.config['UPLOAD_FOLDER'] = os.path.join(PROJECT_ROOT, 'static/uploads')
    
    # Create upload folder if it doesn't exist
    try:
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    except OSError:
        pass
    
    # Initialize database
    db.init_app(app)
    
    # Register blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp)
    
    # Create tables
    with app.app_context():
        db.create_all()
        
        # Create admin user if it doesn't exist
        admin = User.query.filter_by(email='admin@example.com').first()
        if not admin:
            admin = User(
                name='Admin',
                email='admin@example.com',
                is_admin=True
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print("Admin user created: admin@example.com / admin123")
    
    # Create tables - SAFE for new columns
    with app.app_context():
        db.create_all()
    
    # Register main routes
    @app.route('/')
    def index():
        """Home page"""
        return render_template('index.html')
    
    @app.route('/about')
    def about():
        """About page"""
        return render_template('about.html')
    
    # Error handlers
    @app.errorhandler(404)
    def page_not_found(error):
        """Handle 404 errors"""
        return render_template('404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        """Handle 500 errors"""
        return render_template('500.html'), 500

    @app.route('/uploads/<path:filename>')
    def uploaded_file(filename):
        """Serve files from uploads folder - secure with send_from_directory"""
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

    # Context processor to pass user info to templates
    @app.context_processor
    def inject_user():
        """Make user info available in all templates"""
        user_id = session.get('user_id')
        user_name = session.get('user_name')
        is_admin = session.get('is_admin', False)
        
        return {
            'current_user_id': user_id,
            'current_user_name': user_name,
            'is_admin': is_admin,
            'is_logged_in': user_id is not None
        }
    
    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'true').lower() in ('true', '1', 't')
    app.run(debug=debug, host='0.0.0.0', port=port)
