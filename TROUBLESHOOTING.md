# Troubleshooting Guide - Professional Face Security System

## 🔧 Problem 1: Camera Not Showing / Green Light On

### Common Reasons & Fixes:
1. **Camera Permission Denied**
   - Click the 🔒 (lock) icon next to http://127.0.0.1:5000
   - Go to "Site settings" or "Permissions"
   - Find "Camera" and set it to "Allow"
   - Refresh the page!

2. **Webcam in Use by Another App**
   - Close: Zoom, Teams, Skype, Discord, or any other app using your camera
   - Refresh the page and try again

3. **No Webcam Connected**
   - Make sure your webcam is plugged in (if external)
   - For laptops: make sure your camera isn't disabled in BIOS/settings

4. **Browser Issue**
   - Try a different browser: Chrome, Edge, Firefox, or Safari
   - Make sure your browser is up to date

---

## 🔧 Problem 2: Training Doesn't Work

### What's Happening:
The `face_recognition_models` package is still installing in the background! It needs to download a 100MB AI model file, which can take a few minutes.

### Fixes:
1. **Wait for Installation** - just let it finish!
2. **Or Run Training Directly** - open a new terminal and run:
   ```bash
   cd "c:\Users\getas\Downloads\face recognition"
   python train.py
   ```
3. **Check if Packages are Installed** - run:
   ```bash
   pip list | findstr face
   ```

---

## 🔧 Step-by-Step Fix for Camera:
### For Chrome/Edge:
1. Go to **http://127.0.0.1:5000/capture** OR **http://127.0.0.1:5000/recognize-live**
2. Look at the **left side of the address bar** - you should see a 🔒 lock icon or a 🚫 camera icon
3. Click that icon
4. Find "Camera" in the permissions list
5. Change it from "Blocked" to **"Allow"**
6. Click "Reload" or refresh the page manually

### For Firefox:
1. Go to the page
2. Click the 🔒 lock icon
3. Click "Connection secure" → "More information"
4. Go to the "Permissions" tab
5. Find "Use the camera" and set to "Allow"
6. Refresh the page

---

## 🔧 What the "Green Light" Means:
If your webcam has a green light on, that means:
✅ **Your camera is working!**
✅ **It's powered on!**

Just fix the permission issue and you'll see the video feed!

---

## 🔧 Quick Test:
1. Open the **Windows Camera app** (search for "Camera" in Start menu)
2. If you see yourself there, your camera is working perfectly!
3. Then go back to our system and fix the browser permissions!

---

## 🔧 If Training Still Doesn't Work:
Wait 5-10 more minutes for the packages to finish installing, then try again!

---

## ✅ Once Everything is Working:
1. Capture 5+ photos
2. Train the model
3. Use live recognition!
