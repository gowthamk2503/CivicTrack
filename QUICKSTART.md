# Quick Start Guide - Road Maintenance Portal

## ⚡ 30 Second Start (Windows)

1. **Double-click** `setup.bat` (blue file icon)
2. **Wait for completion** (takes 1-2 minutes)
3. **Double-click** `run.bat` (blue file icon)
4. **Open browser**: Go to `http://localhost:5000`
5. **Login**: 
   - Email: `admin@example.com`
   - Password: `admin123`

That's it! 🎉

---

## ⚡ 30 Second Start (Mac/Linux)

1. **Open Terminal** in the project folder
2. **Run**: `bash setup.sh` (first time only)
3. **Run**: `bash run.sh`
4. **Open browser**: Go to `http://localhost:5000`
5. **Login**: 
   - Email: `admin@example.com`
   - Password: `admin123`

---

## 📱 What You Can Do

### As a Regular User
✅ Register a new account  
✅ Report road issues with photos  
✅ Track complaint status  
✅ View all your complaints  

### As an Admin
✅ Login as `admin@example.com` / `admin123`  
✅ View all complaints  
✅ Update complaint status  
✅ Delete complaints  
✅ View statistics & analytics  

---

## 🆘 Quick Troubleshooting

### Setup fails on Windows
- Ensure Python is installed: https://www.python.org/
- Check "Add Python to PATH" during installation
- Delete `venv` folder and try again

### Port 5000 already in use
- Open `app.py`
- Change `port=5000` to `port=5001` (line at bottom)
- Try again

### Application won't start
- Right-click `run.bat` → "Run as Administrator"
- Or delete `database.db` and try again

---

## 📚 Project Files Overview

- **app.py** - Main application file
- **models.py** - Database structure
- **config.py** - Settings
- **routes/** - User & Admin pages
- **templates/** - HTML pages
- **static/** - CSS & JavaScript
- **uploads/** - User uploaded photos

---

## 🔑 Admin Credentials

**Email:** `admin@example.com`  
**Password:** `admin123`

⚠️ **Change these in production!**

---

## 🌐 Browser Dashboard

After login, you'll see:

**Regular Users:**
- Home page
- Report Issue button
- My Complaints list
- View complaint details

**Admins:**
- Dashboard with stats
- All Complaints management
- Status update controls
- Delete functionality
- Detailed statistics

---

## 💾 Database

The app automatically creates `database.db` on first run.  
To reset: Delete `database.db` and restart the app.

---

## 📞 Need Help?

1. Check README.md for detailed documentation
2. Check browser console (F12) for errors
3. Check terminal where app is running

---

**Start the application and enjoy! 🚀**
