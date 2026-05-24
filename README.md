# Face Recognition Security System

A beginner-friendly cybersecurity + face recognition project.

## Project Structure

```
face recognition/
├── app.py          # Main Flask backend application
├── train.py        # Train face recognition model from dataset
├── recognize.py    # Real-time face recognition from webcam
├── requirements.txt # Python dependencies
├── database.db     # SQLite database (auto-created)
├── logs/           # Access logs
├── dataset/        # Training images (add your face images here)
├── models/         # Trained AI models (auto-saved here)
├── static/         # Frontend static files
└── templates/      # HTML templates
```

## Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

**Note**: On Windows, you may need to install CMake and Visual Studio Build Tools first for face_recognition library.

### 2. Add Training Images

Create a folder inside `dataset/` with your name and add your face photos:

```
dataset/
└── your_name/
    ├── 1.jpg
    ├── 2.jpg
    └── ...
```

### 3. Train the Model

```bash
python train.py
```

### 4. Run the Web App

```bash
python app.py
```

Then open your browser and go to http://localhost:5000

### 5. Run Real-time Recognition

```bash
python recognize.py
```

Press 'q' to quit the webcam window.
