# CivicTrack Deployment Guide

This guide details how to deploy the **CivicTrack** web application across different hosting platforms.

---

## 🚀 Option 1: Render.com (Recommended - Free & Easy)

Render offers free web service hosting directly from your GitHub repository.

### Steps:
1. **Push your code to your GitHub repository**:
   ```bash
   git add .
   git commit -m "Add production deployment configurations"
   git push origin main
   ```
2. Go to [Render.com](https://render.com/) and sign in with GitHub.
3. Click **"New +"** and choose **"Web Service"**.
4. Select your **CivicTrack** repository.
5. Configure the service settings:
   - **Name**: `civictrack`
   - **Region**: Choose the closest region (e.g., Singapore, Frankfurt, Oregon)
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn wsgi:app`
   - **Instance Type**: `Free`
6. Under **Environment Variables**, add:
   - `FLASK_ENV`: `production`
   - `SECRET_KEY`: (Click generate or type a random 32+ character string)
7. Click **"Create Web Service"**.
8. Once built, Render will provide a live URL like `https://civictrack.onrender.com`.

> **Note on Free Tier Storage:** On Render's free tier, the filesystem is ephemeral (resets on restart). For long-term persistent storage in production, you can attach a Render PostgreSQL database (set `DATABASE_URL` in environment variables) or use a Render Disk for uploads.

---

## 🚆 Option 2: Railway.app (Persistent Storage & 1-Click)

Railway provides simple deployment and supports persistent volume mounts for uploaded images and SQLite database.

### Steps:
1. Go to [Railway.app](https://railway.app/) and sign in with GitHub.
2. Click **"New Project"** -> **"Deploy from GitHub repo"**.
3. Select your repository.
4. Railway automatically detects `Procfile` / `Dockerfile`.
5. Under **Variables**, add:
   - `PORT`: `5000`
   - `FLASK_ENV`: `production`
   - `SECRET_KEY`: `your-secure-random-secret-key`
6. (Optional) To persist database and image uploads across deployments:
   - Go to your service -> **Volumes** -> **Add Volume**.
   - Mount path: `/app/instance` or `/app/static/uploads`.
7. Click **"Deploy"** and generate a public domain in **Settings** -> **Networking**.

---

## 🐍 Option 3: PythonAnywhere (Free & Great for SQLite)

PythonAnywhere natively supports Flask and persistent SQLite storage.

### Steps:
1. Register for a free account at [PythonAnywhere](https://www.pythonanywhere.com/).
2. Open a **Bash console** on PythonAnywhere and clone your repo:
   ```bash
   git clone https://github.com/gowthamk2503/CivicTrack.git
   cd CivicTrack
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Go to the **Web** tab in PythonAnywhere and click **"Add a new web app"**.
4. Choose **Manual configuration** and select **Python 3.10+**.
5. Set:
   - **Source code**: `/home/yourusername/CivicTrack`
   - **Working directory**: `/home/yourusername/CivicTrack`
   - **Virtualenv**: `/home/yourusername/CivicTrack/venv`
6. Edit the **WSGI configuration file** (link provided on the Web tab) and replace contents with:
   ```python
   import sys
   import os

   path = '/home/yourusername/CivicTrack'
   if path not in sys.path:
       sys.path.append(path)

   from app import create_app
   application = create_app()
   ```
7. Click **"Reload <yourusername>.pythonanywhere.com"** and visit your live site!

---

## 🐳 Option 4: Docker / Self-Hosted VPS (DigitalOcean / AWS / Linode)

If you have a Linux VPS:

### Using Docker Compose:
```bash
# Clone the repository
git clone https://github.com/gowthamk2503/CivicTrack.git
cd CivicTrack

# Build and start container in the background
docker-compose up -d --build
```
Your application will be live on `http://YOUR_SERVER_IP:5000`.

---

## 🔑 Default Admin Account
Upon initial database setup, the admin credentials are:
- **Email**: `admin@example.com`
- **Password**: `admin123`

⚠️ **Important:** Change the admin password or create your own admin account once deployed!
