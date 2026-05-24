# 🎭 Face Recognition Attendance & Security System

A professional, AI-powered face recognition system for attendance tracking, visitor management, and access control. Built with Flask and modern web technologies.

---

## 📋 Table of Contents

- [Features](#features)
- [System Architecture](#system-architecture)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [User Roles](#user-roles)
- [Modules Overview](#modules-overview)
- [Database Schema](#database-schema)
- [API Endpoints](#api-endpoints)
- [Troubleshooting](#troubleshooting)
- [Security Best Practices](#security-best-practices)

---

## ✨ Features

### 🎯 Core Features
- **AI Face Recognition**: Train and recognize faces using machine learning
- **Attendance Tracking**: Automated check-in/check-out with timestamps
- **Visitor Management**: Professional visitor registration and tracking
- **Door Access Control**: Monitor and manage access events
- **Real-time Dashboard**: Live statistics and system overview
- **User Management**: Admin can add, edit, and manage users
- **KYC Verification**: User verification workflow
- **Comprehensive Logging**: All actions logged to database and files

### 🛡️ Security Features
- Role-based access control (RBAC)
- Session management
- Tamper-proof audit trails
- No anonymous access
- Server-side validation

---

## 🏗️ System Architecture

```
face recognition/
├── app.py                    # Main Flask backend application
├── train.py                  # Train face recognition model
├── recognize.py              # Real-time face recognition from webcam
├── check_setup.py            # System setup verification
├── check_accuracy.py         # Model accuracy checker
├── reset_database.py         # Database reset utility
├── update_database.py        # Database migration utility
├── setup_admin.py            # Admin user setup
├── view_trained_data.py      # View trained model data
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables template
├── Dockerfile               # Docker configuration
├── docker-compose.yml       # Docker Compose configuration
├── database.db              # SQLite database (auto-created)
├── logs/                    # Access logs directory
│   └── access.log           # System activity logs
├── dataset/                 # Training images directory
│   └── [username]/          # Individual user's face photos
├── models/                  # Trained AI models directory
│   └── face_model.pkl       # Saved face recognition model
├── static/                  # Frontend static files
└── templates/               # HTML templates
    ├── login.html
    ├── dashboard.html
    ├── user_dashboard.html
    ├── attendance.html
    ├── visitors.html
    ├── door_access.html
    ├── capture.html
    ├── trained_data.html
    ├── recognize_live.html
    ├── user_management.html
    └── kyc_pending.html
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Python 3.x, Flask |
| **Database** | SQLite |
| **AI/ML** | face-recognition library, NumPy |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Optional** | Supabase (cloud database) |

---

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- Webcam (for face capture and recognition)
- Camera permissions enabled in browser

### Step 1: Clone or Download the Project

```bash
cd "c:\Users\getas\Downloads\face recognition"
```

### Step 2: Create Virtual Environment (Recommended)

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Important Note for Windows Users:**

The `face-recognition` library requires:
- CMake
- Visual Studio Build Tools

If you encounter installation issues:
1. Download and install [CMake](https://cmake.org/download/)
2. Download and install [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
3. Select "Desktop development with C++" during installation
4. Restart your terminal and try again

### Step 4: Configure Environment (Optional)

Copy `.env.example` to `.env` and configure if needed:
```bash
cp .env.example .env
```

---

## ⚡ Quick Start

### 1. Initialize the System

First, let's set up the admin user and database:

```bash
python setup_admin.py
```

### 2. Start the Application

```bash
python app.py
```

You'll see:
```
 * Running on http://127.0.0.1:5000
```

### 3. Access the System

Open your browser and navigate to: **http://127.0.0.1:5000**

### 4. Log In

Use the default admin credentials:
- **Username**: `admin`
- **Password**: `admin123`

---

## 👥 User Roles

### Administrator (Admin)
**Full System Access**
- ✅ Dashboard with full statistics
- ✅ Attendance System (view all records)
- ✅ Visitor Management
- ✅ Door Access Control
- ✅ Capture & Train (AI model training)
- ✅ User Management (add/edit/verify users)
- ✅ Trained Data Viewer
- ✅ All system settings and logs

### Regular User
**Limited, Role-Based Access**
- ✅ User Dashboard
- ✅ Attendance System (self check-in only)
- ✅ Live Face Recognition
- ❌ Visitor Management
- ❌ Door Access Control
- ❌ Capture & Train (restricted)
- ❌ User Management

---

## 📦 Modules Overview

### 1. 🔐 Login & Authentication
**Purpose**: Secure user authentication
- Password-based login
- Face recognition login (optional)
- Session management
- Login attempt logging

**Default Credentials**:
- Username: `admin`
- Password: `admin123`

---

### 2. 📊 Dashboard
**Purpose**: Central system overview

**Admin Dashboard**:
- Real-time statistics (today's attendance, visitors, access events)
- Quick access to all modules
- Recent activity logs (last 10 events)
- System status overview

**User Dashboard**:
- Personal welcome message
- Quick access to attendance and recognition

---

### 3. 📋 Attendance System
**Purpose**: Automated employee attendance tracking

**Features**:
- One-click check-in
- Automatic timestamp recording
- Prevents duplicate check-ins (once per day)
- Attendance history view
- Admin can view all records
- Users can only view their own records

**How to Use**:
1. Navigate to **Attendance**
2. Click **✓ Check In Now**
3. Your attendance is recorded!

---

### 4. 👥 Visitor Management
**Purpose**: Professional visitor registration

**Features**:
- Visitor name, purpose, and visited person tracking
- Check-in/check-out timestamps
- Visitor history (last 30 records)
- Status tracking (pending, checked_in, checked_out)

**How to Use**:
1. Go to **Visitors**
2. Fill in the visitor form
3. Click **➕ Register Visitor**

---

### 5. 🚪 Door Access Control
**Purpose**: Monitor and manage access events

**Features**:
- Manual access grant/deny
- Access method tracking (face, manual, etc.)
- Door name specification
- Access event history (last 30 records)

**How to Use**:
1. Navigate to **Door Access**
2. Click **✅ Grant Access** or **❌ Deny Access**
3. Event is logged automatically

---

### 6. 📸 Capture & Train (AI Face Recognition)
**Purpose**: Train the AI model for face recognition

**Part A: Capture Photos**
1. Go to **Capture & Train**
2. Allow camera permission in browser
3. Position your face clearly
4. Click **📷 Capture Photo**
5. Take **10-20 photos** for best results!
   - Different angles
   - Different lighting
   - Different expressions

**Part B: Train the Model**
1. After capturing photos, click **⚡ Train Model**
2. Wait for processing (a few seconds)
3. Success message confirms model is trained!

**Tips for Best Recognition**:
- Use good lighting (avoid backlighting)
- Ensure entire face is visible
- Look directly at camera
- Capture in various conditions

---

### 7. 👤 User Management (Admin Only)
**Purpose**: Manage system users

**Features**:
- Add new users
- Edit existing users
- Verify/unverify KYC status
- View user roles and details
- User creation audit logging

**How to Use**:
1. Go to **User Management**
2. Fill in user details (username, password, role, etc.)
3. Click **Add User**
4. Use the verify/unverify buttons for KYC

---

### 8. 📈 Trained Data Viewer (Admin Only)
**Purpose**: View and monitor trained model data

**Features**:
- Total faces encoded
- Number of people in system
- Photo count per person
- View individual photos
- Accuracy estimation

---

### 9. 🎥 Live Face Recognition
**Purpose**: Real-time face verification

**Features**:
- Live camera feed
- Face detection
- Confidence score display
- Verification status

---

## 🗄️ Database Schema

### Users Table
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| username | TEXT | Unique username |
| password | TEXT | User password |
| role | TEXT | User role (admin/user) |
| full_name | TEXT | Full name |
| email | TEXT | Email address |
| kyc_verified | INTEGER | KYC verification status (0/1) |
| created_at | TEXT | Account creation timestamp |

### Attendance Table
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| username | TEXT | Username |
| date | TEXT | Date (YYYY-MM-DD) |
| check_in | TEXT | Check-in time (HH:MM:SS) |
| check_out | TEXT | Check-out time |
| status | TEXT | Attendance status |

### Visitors Table
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| name | TEXT | Visitor name |
| purpose | TEXT | Purpose of visit |
| visit_date | TEXT | Visit date |
| check_in | TEXT | Check-in time |
| check_out | TEXT | Check-out time |
| visited_person | TEXT | Person being visited |
| status | TEXT | Visitor status |

### Door Access Table
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| username | TEXT | Username |
| door_name | TEXT | Door name |
| access_time | TEXT | Access timestamp |
| access_granted | INTEGER | Access granted (0/1) |
| method | TEXT | Access method |

### Access Logs Table
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| timestamp | TEXT | Event timestamp |
| username | TEXT | Username |
| action | TEXT | Action performed |
| status | TEXT | Action status |
| details | TEXT | Additional details |

---

## 🔌 API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | `/login` | Password login |
| GET | `/face-login` | Face recognition login page |
| POST | `/face-login-auth` | Face recognition authentication |
| GET | `/logout` | Logout user |

### Pages
| Method | Endpoint | Description | Access |
|--------|----------|-------------|--------|
| GET | `/dashboard` | Dashboard | All users |
| GET | `/attendance` | Attendance page | All users |
| GET | `/visitors` | Visitors page | Admin only |
| GET | `/door-access` | Door access page | Admin only |
| GET | `/capture` | Capture photos | All users |
| GET | `/recognize-live` | Live recognition | All users |
| GET | `/user-management` | User management | Admin only |
| GET | `/trained-data` | Trained data view | Admin only |
| GET | `/kyc-pending` | KYC pending page | Users |

### API Routes
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/add-user` | Add new user |
| POST | `/api/save-photo` | Save captured photo |
| POST | `/api/train` | Train face model |
| POST | `/api/attendance/checkin` | Attendance check-in |
| POST | `/api/visitors/add` | Add visitor |
| POST | `/api/door/access` | Door access event |
| POST | `/api/verify-face` | Verify face |
| POST | `/api/check-accuracy` | Check model accuracy |
| POST | `/api/verify-kyc/<id>` | Verify user KYC |
| POST | `/api/unverify-kyc/<id>` | Unverify user KYC |

---

## 🔧 Troubleshooting

### Issue: Webcam not showing
**Solutions**:
- Close other apps using the camera (Zoom, Teams, etc.)
- Refresh the page and allow camera permission
- Check browser camera settings

### Issue: "Failed to fetch" when training
**Solutions**:
- Wait a few minutes (packages might be installing)
- Refresh the page and try again
- Check if server is still running

### Issue: Can't log in
**Solutions**:
- Use default credentials: admin / admin123
- Check if server is running in terminal
- Check for typos in username/password

### Issue: Server not starting
**Solutions**:
- Make sure you're in the correct directory
- Run: `python app.py`
- Install Flask: `pip install Flask`

### Issue: face-recognition installation fails on Windows
**Solutions**:
1. Install CMake from https://cmake.org/download/
2. Install Visual Studio Build Tools
3. Select "Desktop development with C++"
4. Restart terminal and try again

### Issue: Model not training
**Solutions**:
- Make sure you've captured at least 1 photo
- Check dataset folder exists
- Check logs in terminal for errors

---

## 🔒 Security Best Practices

### For Production Use
1. **Change Default Password**: Immediately change the admin password
2. **Use HTTPS**: Deploy with SSL/TLS encryption
3. **Strong Secret Key**: Change `app.secret_key` to a secure random string
4. **Password Hashing**: Implement proper password hashing (currently stored as plain text)
5. **Environment Variables**: Store sensitive data in environment variables
6. **Regular Backups**: Back up the database regularly
7. **Input Validation**: All inputs are validated server-side

### Current Security Measures
- ✅ No anonymous access - all routes require login
- ✅ Role-based access control (RBAC)
- ✅ Comprehensive audit logging (database + file)
- ✅ Session management
- ✅ Server-side validation

---

## 📚 Additional Documentation

- [HOW_TO_USE.md](./HOW_TO_USE.md) - Step-by-step usage guide
- [PURPOSE_AND_ROLES.md](./PURPOSE_AND_ROLES.md) - System purpose and user roles
- [PROFESSIONAL_WORKFLOW.md](./PROFESSIONAL_WORKFLOW.md) - Professional workflow guide
- [MODEL_TRAINING_PURPOSE.md](./MODEL_TRAINING_PURPOSE.md) - Model training guide
- [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) - Detailed troubleshooting

---

## 🎯 Business Use Cases

### 1. Office/Small Business
- Employee attendance tracking
- Office access control
- Visitor management

### 2. School/University
- Student attendance
- Campus security
- Visitor tracking

### 3. Co-working Space
- Member access control
- Visitor management
- Attendance tracking

### 4. Secure Facility
- High-security area access
- Complete audit trail
- Real-time monitoring

---

## 🤝 Contributing

This is a professional face recognition attendance system. Feel free to:
- Report bugs
- Suggest features
- Improve documentation

---

## 📄 License

This project is for educational and professional use.

---

## 🎉 Ready to Use!

Your Face Recognition Attendance & Security System is now ready!

**Next Steps**:
1. Log in with admin credentials
2. Explore the dashboard
3. Capture your face photos
4. Train the AI model
5. Start using the system!

---

**Need Help?** Check the [Troubleshooting](#troubleshooting) section or refer to the additional documentation files.
