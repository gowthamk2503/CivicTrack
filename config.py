import os
from datetime import timedelta

# Get the absolute path to the project root (where config.py is located)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

IS_VERCEL = bool(os.environ.get('VERCEL'))

class Config:
    """Base configuration"""
    db_url = os.environ.get('DATABASE_URL')
    if db_url:
        if db_url.startswith('postgres://'):
            db_url = db_url.replace('postgres://', 'postgresql://', 1)
        SQLALCHEMY_DATABASE_URI = db_url
    elif IS_VERCEL:
        SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/database.db'
    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-change-in-production')
    
    if IS_VERCEL:
        UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', '/tmp/uploads')
    else:
        UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', os.path.join(PROJECT_ROOT, 'static/uploads'))

    MAX_CONTENT_LENGTH = int(os.environ.get('MAX_CONTENT_LENGTH', 16 * 1024 * 1024))
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    
    # Allowed file extensions
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
