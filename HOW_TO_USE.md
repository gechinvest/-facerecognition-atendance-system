# How to Work the Professional Face Security System

## 🚀 Quick Start Guide

### Step 1: Start the System
1. Open your terminal/command prompt
2. Go to the project folder: `cd "c:\Users\getas\Downloads\face recognition"`
3. Run: `python app.py`
4. You'll see: `Running on http://127.0.0.1:5000`

---

### Step 2: Log In
1. Open your browser (Chrome, Edge, Firefox, etc.)
2. Go to: **http://127.0.0.1:5000**
3. Enter login credentials:
   - Username: `admin`
   - Password: `admin123`
4. Click "Login"

---

### Step 3: Explore the Dashboard
After logging in, you'll see the **Professional Dashboard** with:
- 📊 Real-time statistics
- 4 quick-access module cards
- Recent system activity logs

---

## 📋 Using Each Module

---

### Module 1: 📋 Attendance System
**How to use:**
1. Click **Attendance** in the top navigation bar OR click the 📋 module card
2. To check in: Click the **✓ Check In Now** button
3. You'll see your attendance record appear in the table
4. You can only check in **once per day**

---

### Module 2: 👥 Visitor Management
**How to use:**
1. Click **Visitors** in the top navigation bar OR click the 👥 module card
2. Fill in the visitor form:
   - **Visitor Name** (required): Enter visitor's full name
   - **Purpose of Visit** (optional): Meeting, delivery, interview, etc.
   - **Visiting Person** (optional): Who the visitor is here to see
3. Click **➕ Register Visitor**
4. The visitor will appear in the visitors table below

---

### Module 3: 🚪 Door Access Control
**How to use:**
1. Click **Door Access** in the top navigation bar OR click the 🚪 module card
2. To grant access: Click **✅ Grant Access**
3. To deny access: Click **❌ Deny Access**
4. The access event will appear in the door access logs table

---

### Module 4: 📸 Capture & Train (AI Face Recognition)
**This is the most important module for face recognition!**

#### Part A: Capture Training Photos
1. Click **Capture & Train** in the top navigation bar OR click the 📸 module card
2. Your browser will ask for **camera permission** - click **Allow**
3. You'll see your webcam feed on the left
4. Position your face clearly in the camera
5. Click **📷 Capture Photo** to take a picture
6. The photo will appear on the right, and the count will increase
7. **Take 10-20 photos** for best recognition results!
   - Different angles (left, right, straight)
   - Different lighting
   - Different expressions (smiling, neutral)

#### Part B: Train the AI Model
1. Once you have 10+ photos captured, click **⚡ Train Model**
2. Wait a few seconds while the system processes all photos
3. You'll see a success message when training is complete!
4. The model is now saved and ready to use!

---

### Step 4: Log Out
When you're done:
1. Click **Logout** in the top navigation bar
2. You'll be returned to the login page
3. Your session is securely closed

---

## 💡 Pro Tips for Best Results

### For Better Face Recognition
- Take **15-20 photos** per person
- Capture in **good lighting** (avoid backlighting)
- Make sure your **entire face is visible**
- Look directly at the camera for most photos
- Include some photos with slight angles

### For System Efficiency
- Check in to attendance once per day
- Register visitors as they arrive
- Train the model after adding new people or more photos
- Use the dashboard to monitor recent activity

---

## 🔍 Troubleshooting Common Issues

### Issue: Webcam not showing
- **Fix**: Make sure no other app is using your camera (Zoom, Teams, etc.)
- **Fix**: Refresh the page and allow camera permission again
- **Fix**: Check your browser settings to make sure camera access is allowed

### Issue: "Failed to fetch" when training
- **Fix**: Wait a few minutes - the packages were probably still installing
- **Fix**: Refresh the page and try again
- **Fix**: The packages are now installed, so it should work!

### Issue: Can't log in
- **Fix**: Make sure you're using: Username = `admin`, Password = `admin123`
- **Fix**: Check that the server is still running (look at your terminal)

### Issue: Server not starting
- **Fix**: Make sure you're in the right folder: `cd "c:\Users\getas\Downloads\face recognition"`
- **Fix**: Run: `python app.py`
- **Fix**: Make sure Flask is installed: `pip install Flask`

---

## 📊 What the System Tracks

Every action you take is automatically logged:
- Logins and logouts
- Attendance check-ins
- Visitor registrations
- Door access grants/denials
- Photo captures
- AI model training

All logs are stored in:
1. The SQLite database (`database.db`)
2. A text file (`logs/access.log`)

---

## 🎉 You're Ready!

Your Professional Face Recognition Security System is now **100% ready to use**!

Start with:
1. Logging in
2. Exploring the dashboard
3. Capturing photos and training the model!

Enjoy your professional security system! 🚀
