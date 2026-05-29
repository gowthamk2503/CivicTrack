# Citizen Feedback on Road Maintenance

A complete full-stack Python web application where citizens can report road maintenance issues and admins can manage resolutions.

## 🎯 Features

### User Features
- **User Registration & Login** - Secure authentication with password hashing
- **Submit Complaints** - Report road issues with:
  - Title and detailed description
  - Photo upload with preview
  - Location information
- **Track Complaints** - Monitor complaint status in real-time:
  - Pending (Red)
  - In Progress (Yellow)
  - Resolved (Green)
- **View History** - See all submitted complaints with pagination

### Admin Features
- **Admin Dashboard** - Overview of complaint statistics:
  - Total complaints
  - Pending, In Progress, and Resolved counts
  - Quick action buttons
- **Manage Complaints** - View all complaints with filtering
- **Update Status** - Change complaint status and track progress
- **Delete Complaints** - Remove complaints if needed
- **Statistics** - Detailed analytics:
  - Resolution progress charts
  - Top problem areas
  - User and complaint statistics

### Security Features
- Password hashing with Werkzeug
- Input validation
- Session-based authentication
- Protected admin routes
- CSRF protection

## 🛠 Tech Stack

- **Backend**: Flask 2.3.3
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **JavaScript**: Vanilla JS with Bootstrap utilities
- **File Storage**: Local uploads folder

## 📁 Project Structure

```
citizen_project/
├── app.py              # Main Flask application
├── config.py           # Configuration settings
├── models.py           # Database models (User, Complaint)
├── requirements.txt    # Python dependencies
├── database.db         # SQLite database (generated on first run)
├── routes/
│   ├── __init__.py
│   ├── user_routes.py  # User authentication & complaint routes
│   └── admin_routes.py # Admin dashboard & management routes
├── templates/
│   ├── base.html       # Base template with navigation
│   ├── index.html      # Home page
│   ├── about.html      # About page
│   ├── register.html   # Registration page
│   ├── login.html      # Login page
│   ├── complaint_form.html      # Submit complaint form
│   ├── user_dashboard.html      # User's complaints list
│   ├── complaint_detail.html    # Individual complaint details
│   ├── admin_dashboard.html     # Admin dashboard
│   ├── admin_complaints.html    # Admin manage complaints
│   ├── admin_statistics.html    # Admin analytics
│   ├── 404.html        # Not found page
│   └── 500.html        # Server error page
├── static/
│   ├── css/
│   │   └── style.css   # Custom styles
│   └── js/
│       └── script.js   # JavaScript utilities
├── uploads/            # User uploaded images
└── README.md           # This file
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Windows/Mac/Linux

### Step 1: Extract Project Files
Navigate to the project directory:
```bash
cd c:\Users\vijay\OneDrive\Desktop\citizen_project
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```

The application will start on `http://localhost:5000`

## 📖 Usage Guide

### First Time Setup
1. The application automatically creates an admin user on first run:
   - **Email**: `admin@example.com`
   - **Password**: `admin123`

2. Open browser and navigate to `http://localhost:5000`

### For Citizens

#### Register
1. Click "Register" in the top menu
2. Enter name, email, and password (min 6 characters)
3. Confirm password and submit
4. Login with your credentials

#### Report an Issue
1. After login, click "Submit New" or "Report an Issue"
2. Fill in the form:
   - **Title**: Brief description (e.g., "Large pothole on Main Street")
   - **Description**: Detailed information about the issue
   - **Location**: Street name or address
   - **Photo**: Upload an image (PNG, JPG, JPEG, GIF - Max 16MB)
3. Click "Submit Complaint"
4. You'll be redirected to your complaints list

#### Track Complaints
1. Click "My Complaints" to see all your reports
2. Click "View Details" to see full information
3. Monitor status changes as authorities work on the issue

### For Admins

#### Access Admin Panel
1. Login with admin credentials
2. You'll be redirected to Admin Dashboard

#### Dashboard
- View statistics about all complaints
- See counts for Pending, In Progress, and Resolved
- Quick access to all complaints and detailed statistics

#### Manage Complaints
1. Go to "All Complaints" from Admin menu
2. Filter by status (Pending, In Progress, Resolved)
3. Click edit button to update status
4. Click delete button to remove a complaint (with confirmation)

#### View Statistics
1. Click "Statistics" in Admin menu
2. See resolution progress with visual charts
3. View top problem areas with complaint counts

## 🔑 Default Credentials

**Admin Account:**
- Email: `admin@example.com`
- Password: `admin123`

⚠️ **IMPORTANT**: Change these credentials in production!

## 📋 API Routes

### User Routes
- `GET /` - Home page
- `GET /about` - About page
- `GET/POST /register` - User registration
- `GET/POST /login` - User login
- `GET /logout` - User logout
- `GET/POST /submit-complaint` - Submit new complaint
- `GET /view-complaints` - View user's complaints (paginated)
- `GET /complaint/<id>` - View complaint details

### Admin Routes
- `GET /admin/dashboard` - Admin dashboard
- `GET /admin/complaints` - View all complaints (with filtering)
- `POST /admin/complaint/<id>/update-status` - Update complaint status
- `POST /admin/complaint/<id>/delete` - Delete complaint
- `GET /admin/statistics` - View detailed statistics

## 🎨 Customization

### Change Admin Credentials
Edit `app.py` in the `create_app()` function:
```python
# Change these values
admin = User(
    name='Your Admin Name',
    email='youremail@example.com',
    is_admin=True
)
admin.set_password('yourpassword')
```

### Change Theme Colors
Edit `static/css/style.css` - Modify CSS variables in `:root` selector

### Customize Flask Settings
Edit `config.py` to adjust:
- `MAX_CONTENT_LENGTH` - File upload size limit
- `ALLOWED_EXTENSIONS` - Allowed file types
- `UPLOAD_FOLDER` - Folder for uploaded images
- `SECRET_KEY` - Session key (change in production)

## 🔒 Security Notes

1. **Change Secret Key**: In production, change `SECRET_KEY` in `config.py`
2. **Change Admin Password**: Update default admin credentials
3. **Enable HTTPS**: Use HTTPS in production
4. **Database**: Consider using PostgreSQL instead of SQLite for production
5. **Validation**: All inputs are validated server-side

## 🐛 Troubleshooting

### Port Already in Use
If port 5000 is already in use, modify `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Change port number
```

### Database Issues
To reset the database:
1. Delete `database.db` file
2. Run `python app.py` again to create fresh database

### Upload Issues
- Check `uploads/` folder exists
- Ensure proper file permissions
- Verify file size is less than 16MB

### Session Issues
- Clear browser cookies
- Ensure cookies are enabled
- Check browser's storage settings

## 📚 Dependencies

- **Flask**: Web framework
- **Flask-SQLAlchemy**: ORM for database
- **Werkzeug**: Security utilities (password hashing)
- **python-dotenv**: Environment variables (optional)

## 🎓 Learning Resources

This project demonstrates:
- Flask web framework fundamentals
- SQLAlchemy ORM usage
- User authentication and authorization
- File upload handling
- Bootstrap responsive design
- RESTful API concepts
- Database modeling
- Session management

## 📝 Future Enhancements

Potential features to add:
- Email notifications for updates
- Map integration (Google Maps/Leaflet)
- Admin user management
- Comment/discussion on complaints
- Photo gallery for complaints
- Export reports to PDF
- SMS notifications
- Mobile app
- Real-time updates with WebSockets

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review Flask documentation: https://flask.palletsprojects.com/
3. Check SQLAlchemy docs: https://docs.sqlalchemy.org/

## 📄 License

This project is provided as-is for educational purposes.

## ✅ Checklist for Running

- [ ] Python 3.8+ installed
- [ ] Project files extracted
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Navigate to project folder
- [ ] Run `python app.py`
- [ ] Open browser to `http://localhost:5000`
- [ ] Login with admin@example.com / admin123
- [ ] Test user registration
- [ ] Test complaint submission
- [ ] Test admin functions

---

**Happy Coding! 🚀**

For issues with the road maintenance system, please report them through the application!
