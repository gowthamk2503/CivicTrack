# Installation Guide - Windows

## Prerequisites Check

Before starting, ensure you have:
- ✅ Windows 10 or later
- ✅ Internet connection
- ✅ Administrator access (recommended)
- ✅ At least 500MB free disk space

---

## Step 1: Install Python

### Option A: Download from python.org (Recommended)

1. Go to https://www.python.org/downloads/
2. Click "Download Python 3.12" (or latest 3.x version)
3. **Important**: Check ✅ "Add Python to PATH"
4. Click "Install Now"
5. Wait for installation to complete
6. Click "Close"

### Option B: Using Microsoft Store

1. Open Microsoft Store
2. Search for "Python"
3. Install from official Microsoft Python release

### Verify Installation

1. Press `Win + R`
2. Type: `cmd`
3. In Command Prompt, type: `python --version`
4. You should see something like `Python 3.12.x`

If you get an error → Python is not installed or not in PATH. Reinstall and check the "Add Python to PATH" option.

---

## Step 2: Extract Project Files

The project should already be in:
```
C:\Users\vijay\OneDrive\Desktop\citizen_project
```

If not, extract the ZIP file here.

---

## Step 3: Run Setup Script

### Using Explorer (Easiest)

1. Open File Explorer
2. Navigate to `C:\Users\vijay\OneDrive\Desktop\citizen_project`
3. **Double-click** `setup.bat` file (blue icon)
4. A Command Prompt window will open
5. Wait for "Setup Complete!" message
6. Press any key to close

### Using Command Prompt (Manual)

1. Press `Win + R`
2. Type: `cmd` and press Enter
3. Type:
   ```
   cd C:\Users\vijay\OneDrive\Desktop\citizen_project
   setup.bat
   ```
4. Wait for completion
5. Close the window

---

## Step 4: Run the Application

### Using Explorer (Easiest)

1. **Double-click** `run.bat` file (blue icon)
2. A Command Prompt window will open
3. You'll see: `Running on http://127.0.0.1:5000`
4. Open your browser to: `http://localhost:5000`

### Using Command Prompt (Manual)

1. Press `Win + R`
2. Type: `cmd` and press Enter
3. Type:
   ```
   cd C:\Users\vijay\OneDrive\Desktop\citizen_project
   run.bat
   ```
4. You'll see: `Running on http://127.0.0.1:5000`
5. Open browser to: `http://localhost:5000`

---

## Step 5: Login & Explore

### First Login (Admin)

1. Browser automatically opens to `http://localhost:5000`
2. Click "Login" in the top menu
3. Enter:
   - Email: `admin@example.com`
   - Password: `admin123`
4. Click "Login"

### Create User Account (Optional)

1. Go back to Home (`http://localhost:5000`)
2. Click "Register"
3. Enter your details:
   - Full Name: Your name
   - Email: Your email
   - Password: At least 6 characters
   - Confirm Password: Same as above
4. Click "Register"
5. Click "Login" and enter your new credentials

---

## What's Happening Behind the Scenes

### setup.bat does:
1. ✅ Creates a Python virtual environment (venv folder)
2. ✅ Installs required packages from requirements.txt
3. ✅ Prepares the project for running

### run.bat does:
1. ✅ Activates the virtual environment
2. ✅ Starts the Flask web server
3. ✅ Makes the app available at http://localhost:5000
4. ✅ Automatically creates database.db on first run

---

## Stopping the Application

### Method 1: Close the Command Prompt window

Simply close the black Command Prompt window where the app is running.

### Method 2: Keyboard shortcut

In the Command Prompt window, press: `Ctrl + C`

Then type: `Y` and press Enter

---

## Troubleshooting

### Problem: "Python is not installed or not in PATH"

**Solution:**
1. Uninstall Python from Control Panel
2. Download from https://www.python.org/downloads/
3. During installation, CHECK ✅ "Add Python to PATH"
4. Click "Install Now"
5. After installation, restart your computer
6. Try `setup.bat` again

### Problem: "'pip' is not recognized"

**Solution:**
1. Reinstall Python with "Add Python to PATH" checked
2. Restart computer
3. Try again

### Problem: "Port 5000 already in use"

**Solution:**
1. Open `app.py` with Notepad
2. Find the last line: `app.run(debug=True, host='0.0.0.0', port=5000)`
3. Change `5000` to `5001`:
   ```python
   app.run(debug=True, host='0.0.0.0', port=5001)
   ```
4. Save the file (Ctrl + S)
5. Try `run.bat` again
6. Go to `http://localhost:5001`

### Problem: Setup fails and asks to run manually

**Solution - Manual Installation:**

1. Press `Win + R`
2. Type: `cmd` and press Enter
3. Run each command separately:
   ```
   cd C:\Users\vijay\OneDrive\Desktop\citizen_project
   python -m venv venv
   venv\Scripts\activate.bat
   pip install -r requirements.txt
   ```
4. Once complete, type: `python app.py`
5. Open browser to `http://localhost:5000`

### Problem: Can't open http://localhost:5000

**Solution:**
1. Make sure the Command Prompt shows: `Running on http://127.0.0.1:5000`
2. Copy the exact URL and paste in browser
3. If still doesn't work:
   - Try `http://127.0.0.1:5000` instead
   - Try `http://0.0.0.0:5000`
   - Check if firewall is blocking (allow through Windows Defender)

### Problem: "Module not found" error

**Solution:**
1. Make sure you're in the `venv` environment
2. Check that `requirements.txt` exists in the project folder
3. Run: `pip install -r requirements.txt`
4. Try running the app again

---

## File Structure Explained

```
citizen_project/
│
├── setup.bat          ← Double-click to install (first time only)
├── run.bat            ← Double-click to start app
│
├── app.py             ← Main application file
├── models.py          ← Database definitions
├── config.py          ← Settings
│
├── routes/            ← User & Admin pages logic
│   ├── user_routes.py
│   └── admin_routes.py
│
├── templates/         ← HTML pages (what you see in browser)
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── ...
│
├── static/            ← CSS & JavaScript styling
│   ├── css/style.css
│   └── js/script.js
│
├── uploads/           ← User uploaded photos (auto-created)
│
├── database.db        ← Database file (auto-created)
└── requirements.txt   ← Python packages needed
```

---

## How to Use the Application

### As a Regular Citizen

1. **Register**: Create a free account
2. **Login**: Use your credentials
3. **Report Issue**: Click "Report an Issue"
   - Add title, description, location, and photo
   - Click "Submit Complaint"
4. **Track**: View "My Complaints"
   - See status updates (Pending → In Progress → Resolved)
5. **Details**: Click on any complaint to see full details

### As Admin

1. **Login**: admin@example.com / admin123
2. **Dashboard**: See all statistics
3. **Manage**: Go to "All Complaints"
4. **Update**: Click edit button to change status
5. **Delete**: Click delete button (with confirmation)
6. **Analytics**: View "Statistics" for insights

---

## Security Notes

### For Development (Safe)
- Current setup is fine for learning
- Admin password is default

### For Production (Important)
- Change admin password immediately
- Change SECRET_KEY in config.py
- Use HTTPS instead of HTTP
- Move database to production database (PostgreSQL, MySQL)
- Set DEBUG = False

---

## Uninstalling / Cleaning Up

To completely remove (keep original files):

1. Delete the `venv` folder
2. Delete `database.db` file
3. Application files remain untouched

To reinstall:
1. Run `setup.bat` again

---

## Next Steps

1. ✅ Run setup.bat
2. ✅ Run run.bat
3. ✅ Open http://localhost:5000
4. ✅ Register as citizen or login as admin
5. ✅ Explore the application
6. ✅ Read README.md for detailed features
7. ✅ Try adding features or customizing

---

## Help & Support

### Common Questions

**Q: Do I need internet to run the app?**
A: No, only for initial setup. Once running, offline access works.

**Q: Can multiple people use it?**
A: Yes, on the same network at `http://<your-ip>:5000`

**Q: Is my data safe?**
A: Yes, it's stored locally in database.db. Only you have access.

**Q: How do I backup my data?**
A: Copy `database.db` file to another location.

---

**You're all set! Start with double-clicking setup.bat! 🚀**
