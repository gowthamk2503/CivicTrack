<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=32&pause=1000&color=EF4444&center=true&vCenter=true&width=700&lines=🚧+CivicTrack;Smart+Road+Issue+Reporting;Building+Better+Cities+Together!" alt="Typing SVG" />

<br/>

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logoColor=white" />
  <img src="https://img.shields.io/badge/Bootstrap_5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" />
</p>

<br/>

> **CivicTrack** empowers citizens to report road issues with image evidence, track complaint progress in real time, and enables authorities to manage and resolve infrastructure problems efficiently — all from one platform.

<br/>

<a href="https://github.com/gowthamk2503/CivicTrack">
  <img src="https://img.shields.io/badge/⭐ Star on GitHub-Support the Project-24292e?style=for-the-badge&logo=github" />
</a>

</div>

---

## 📸 Screenshots

<div align="center">

| 🏠 Home Page | 📝 Complaint Form |
|:---:|:---:|
| ![Home](https://github.com/user-attachments/assets/c6ed34fc-0456-4013-9cb5-bb898815a934) | ![Complaint](https://github.com/user-attachments/assets/61540898-916d-4342-be19-49499abff3eb) |

| ⚙️ Admin Dashboard | 📈 Analytics |
|:---:|:---:|
| ![Admin](https://github.com/user-attachments/assets/b7012093-7d6c-4a57-9fc1-c20a8cfa5787) | ![Analytics](https://github.com/user-attachments/assets/ac6a6752-bd72-45cc-a28b-aae8cdbe99e6) |

</div>

---

## 🌍 The Problem We're Solving

Traditional road complaint systems are broken:

```
❌ Manual forms → Delayed registration
❌ No tracking  → Zero transparency
❌ Siloed data  → No central management
❌ No analytics → Poor infrastructure planning
❌ No feedback  → Citizens left in the dark
```

**CivicTrack fixes all of this** with a modern web platform that connects citizens directly to the authorities who can act.

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 👥 Citizen Portal
- 🔐 Secure registration & login
- 📝 Submit road complaints with images
- 📍 Add location information
- 📊 Real-time status tracking
- 📂 Full complaint history
- 🔔 Monitor resolution progress

**Reportable Issues:**
> Potholes · Damaged Roads · Water Logging · Road Cracks · Construction Issues · Traffic Hazards

</td>
<td width="50%">

### 🛡️ Admin Dashboard
- 📊 Live complaint statistics
- 🔍 Filter by status
- ✏️ Update complaint progress
- 🗑️ Remove invalid complaints
- 📈 Analytics & trends
- 👥 User activity insights

**Dashboard Metrics:**
> Total · Pending · In Progress · Resolved

</td>
</tr>
</table>

---

## 📊 Complaint Status System

<div align="center">

| Status | Indicator | Meaning |
|:------:|:---------:|:--------|
| Pending | 🔴 Red | Complaint submitted, awaiting review |
| In Progress | 🟡 Yellow | Authorities are actively working on it |
| Resolved | 🟢 Green | Issue has been fixed and closed |

</div>

---

## 🛠️ Tech Stack

```
┌─────────────────────────────────────────────────────────────────┐
│                        CIVICTRACK STACK                         │
├──────────────────────────┬──────────────────────────────────────┤
│         BACKEND          │            FRONTEND                  │
│──────────────────────────│──────────────────────────────────────│
│  Flask  (Web Framework)  │  HTML5      (Structure)              │
│  SQLAlchemy  (ORM)       │  CSS3       (Styling)                │
│  SQLite  (Database)      │  Bootstrap 5 (Responsive UI)         │
│  Werkzeug  (Auth/Security│  JavaScript  (Dynamic Behavior)      │
└──────────────────────────┴──────────────────────────────────────┘
```

---

## 📂 Project Structure

```bash
CivicTrack/
│
├── 🐍 app.py                    # Application entry point
├── ⚙️  config.py                 # Configuration settings
├── 🗄️  models.py                 # Database models
├── 📋 requirements.txt          # Python dependencies
│
├── 📁 routes/
│   ├── user_routes.py           # Citizen-facing routes
│   └── admin_routes.py          # Admin routes
│
├── 🎨 templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── complaint_form.html
│   ├── user_dashboard.html
│   ├── admin_dashboard.html
│   └── admin_statistics.html
│
├── 🖼️  static/
│   ├── css/
│   └── js/
│
├── 📤 uploads/                  # Uploaded complaint images
└── 📸 screenshots/
```

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/gowthamk2503/CivicTrack.git
cd CivicTrack
```

### 2. Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
# Runs on http://localhost:5000
```

---

## 🔑 Default Admin Credentials

```
Email:    admin@example.com
Password: admin123
```

> ⚠️ **Important:** Change these credentials before any production deployment.

---

## 🔄 Application Workflow

```
👤 Citizen Registers & Logs In
           │
           ▼
    📝 Submits Complaint
    (Title · Description · Location · Image)
           │
           ▼
    🗄️ Stored in Database
           │
           ▼
    🛡️ Admin Reviews Complaint
           │
      ┌────┴────┐
      ▼         ▼
  🟡 In       🟢 Resolved
  Progress
      │
      ▼
  👤 Citizen Tracks Progress → ✅ Issue Closed
```

---

## 🛡️ Security Features

| Feature | Implementation |
|---------|---------------|
| Password Security | Werkzeug hashing |
| Input Validation | Server-side checks |
| Session Auth | Flask session management |
| Admin Protection | Role-based route guards |
| CSRF Protection | Flask-WTF tokens |
| File Upload Safety | Type & size validation |

---

## 🔮 Roadmap

- [ ] 🗺️ Google Maps integration for complaint location pinning
- [ ] 📍 Live complaint map view for citizens
- [ ] 🤖 AI-based road damage detection from uploaded images
- [ ] 📱 GPS auto-location tagging
- [ ] 📧 Email & SMS status notifications
- [ ] 📄 PDF report generation for authorities
- [ ] 🧠 AI complaint prioritization engine
- [ ] 📱 Mobile application (React Native)

---

## 🎯 What I Learned

This project gave me hands-on experience with Flask's application factory pattern, SQLAlchemy ORM design, and session-based authentication flows. Building the admin analytics dashboard pushed me to think about data aggregation queries, while the image upload pipeline taught me secure file handling and validation strategies.

---

## 👨‍💻 Author

<div align="center">

### Gowtham K

🎓 B.Tech Information Technology — Sri Eshwar College of Engineering

[![GitHub](https://img.shields.io/badge/GitHub-gowthamk2503-24292e?style=for-the-badge&logo=github)](https://github.com/gowthamk2503)
[![Email](https://img.shields.io/badge/Email-gowtham.k2023it@sece.ac.in-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:gowtham.k2023it@sece.ac.in)

</div>

---

<div align="center">

### ⭐ Found this useful? Give it a star — it helps more than you think!

*Built with ❤️ to make civic infrastructure smarter, one complaint at a time.*

</div>
