# 🛣️ Citizen Feedback on Road Maintenance System

<div align="center">

<h1>🚧 Citizen Feedback on Road Maintenance</h1>

### Smart Civic Issue Reporting & Road Maintenance Management Platform

A full-stack web application that empowers citizens to report road maintenance issues with image evidence, track complaint progress, and enables government authorities to efficiently manage and resolve civic infrastructure problems.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge\&logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge\&logo=sqlite)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge\&logo=bootstrap)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

### 🌍 Building Better Roads Through Citizen Participation

</div>

---

# 📖 Overview

Road maintenance remains one of the most common challenges faced by cities and municipalities. Traditional complaint reporting methods often involve delays, lack of transparency, and inefficient communication between citizens and authorities.

The **Citizen Feedback on Road Maintenance System** provides a digital platform where citizens can report road-related issues, upload supporting images, track complaint status, and receive updates while administrators efficiently manage complaints through a centralized dashboard.

---

# 🎯 Problem Statement

Current road maintenance reporting systems suffer from:

* Delayed complaint registration
* Lack of transparency
* No centralized complaint management
* Difficulty tracking issue resolution
* Poor communication between citizens and authorities
* Absence of analytics for infrastructure planning

This system addresses these challenges through a modern web-based solution.

---

# 🌟 Key Features

## 👥 Citizen Features

### 🔐 Secure Authentication

* User Registration
* Secure Login System
* Password Encryption
* Session Management

### 📝 Submit Road Complaints

Citizens can report:

* Potholes
* Damaged Roads
* Water Logging
* Road Cracks
* Construction Issues
* Traffic Hazards

Each complaint includes:

* Issue Title
* Detailed Description
* Location Information
* Image Upload

---

### 📊 Complaint Tracking

Track complaint progress with status indicators:

| Status      | Color     |
| ----------- | --------- |
| Pending     | 🔴 Red    |
| In Progress | 🟡 Yellow |
| Resolved    | 🟢 Green  |

---

### 📂 Complaint History

Users can:

* View previous complaints
* Monitor updates
* Access complaint details
* Track resolution progress

---

# ⚙️ Admin Features

## 📊 Admin Dashboard

Real-time dashboard displaying:

* Total Complaints
* Pending Complaints
* In Progress Issues
* Resolved Complaints

---

## 🛠 Complaint Management

Administrators can:

* View all complaints
* Filter complaints by status
* Update complaint progress
* Delete invalid complaints
* Monitor complaint activity

---

## 📈 Analytics & Statistics

Advanced reporting system provides:

* Complaint Distribution
* Resolution Rate
* Top Problem Areas
* User Activity Insights
* Infrastructure Trends

---

# 🛡 Security Features

* Password Hashing using Werkzeug
* Input Validation
* Session-Based Authentication
* Protected Admin Routes
* CSRF Protection
* Secure File Upload Validation

---

# 🛠 Technology Stack

## Backend

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Flask      | Web Framework             |
| SQLAlchemy | ORM                       |
| SQLite     | Database                  |
| Werkzeug   | Authentication & Security |

---

## Frontend

| Technology  | Purpose               |
| ----------- | --------------------- |
| HTML5       | Structure             |
| CSS3        | Styling               |
| Bootstrap 5 | Responsive UI         |
| JavaScript  | Dynamic Functionality |

---

## Storage

| Technology    | Purpose          |
| ------------- | ---------------- |
| Local Storage | Uploaded Images  |
| SQLite        | Application Data |

---

# 📸 Application Screenshots

## 🏠 Home Page

```text
Add Screenshot:
screenshots/home.png
```

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c6ed34fc-0456-4013-9cb5-bb898815a934" />


---

## 📝 Complaint Submission

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/61540898-916d-4342-be19-49499abff3eb" />


---


## ⚙️ Admin Dashboard

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b7012093-7d6c-4a57-9fc1-c20a8cfa5787" />


---

## 📈 Analytics Dashboard

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ac6a6752-bd72-45cc-a28b-aae8cdbe99e6" />


---



# 🏗 System Architecture

```text
Citizen
   │
   ▼
Complaint Submission
   │
   ▼
Flask Backend
   │
   ▼
SQLite Database
   │
   ▼
Admin Dashboard
   │
   ▼
Complaint Processing
   │
   ▼
Status Updates
   │
   ▼
Citizen Notification
```

---

# 📂 Project Structure

```bash
Citizen-Feedback-System/
│
├── app.py
├── config.py
├── models.py
├── requirements.txt
│
├── routes/
│   ├── user_routes.py
│   └── admin_routes.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── complaint_form.html
│   ├── user_dashboard.html
│   ├── admin_dashboard.html
│   └── admin_statistics.html
│
├── static/
│   ├── css/
│   └── js/
│
├── uploads/
├── screenshots/
└── README.md
```

---

# 🚀 Installation & Setup

## Clone Repository

```bash
git clone https://github.com/gowthamk2503/CivicTrack.git
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python app.py
```

Application runs at:

```bash
http://localhost:5000
```

---

# 🔑 Default Admin Credentials

```text
Email: admin@example.com
Password: admin123
```

⚠️ Change these credentials before production deployment.

---

# 📋 Application Workflow

```text
Citizen Registration
        │
        ▼
User Login
        │
        ▼
Submit Complaint
        │
        ▼
Upload Image Evidence
        │
        ▼
Store in Database
        │
        ▼
Admin Review
        │
        ▼
Status Update
        │
        ▼
Citizen Tracks Progress
        │
        ▼
Complaint Resolution
```

---

# 📊 Future Enhancements

### 🌍 Smart City Features

* Google Maps Integration
* Live Complaint Mapping
* AI-Based Road Damage Detection
* GPS Location Tracking
* Mobile Application
* Real-Time Notifications
* SMS Alerts
* Email Updates
* PDF Report Generation
* Complaint Prioritization using AI

---

# 🎓 Learning Outcomes

This project demonstrates:

✅ Flask Development

✅ Database Design

✅ SQLAlchemy ORM

✅ Authentication Systems

✅ File Upload Handling

✅ Admin Dashboard Development

✅ Data Analytics

✅ Responsive Web Design

✅ Civic Technology Solutions

---

# 🌟 Why This Project?

The Citizen Feedback on Road Maintenance System promotes transparency and citizen participation by enabling direct communication between the public and local authorities.

The platform helps:

* Improve road quality
* Reduce complaint resolution time
* Increase government accountability
* Support smart city initiatives
* Enhance citizen engagement

---

# 👨‍💻 Author

## Gowtham K

🎓 B.Tech Information Technology
🏫 Sri Eshwar College of Engineering

📧 [gowtham.k2023it@sece.ac.in](mailto:gowtham.k2023it@sece.ac.in)

### 🌐 Connect With Me

* GitHub
* LinkedIn
* Portfolio

---

# 📜 License

This project is licensed under the MIT License.

---

<div align="center">

## ⭐ If you found this project useful, give it a Star ⭐

### 🚧 Building Smarter Cities Through Technology 🚧

</div>
