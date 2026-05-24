import face_recognition
import cv2
import os
import pickle
import datetime
import sqlite3

def load_model():
    model_path = os.path.join('models', 'face_model.pkl')
    if not os.path.exists(model_path):
        print(f"Model not found at {model_path}. Please run train.py first.")
        return None, None
    
    with open(model_path, 'rb') as f:
        data = pickle.load(f)
    
    return data['encodings'], data['names']

def log_access(username, status):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO access_logs (timestamp, username, action, status, details) VALUES (?, ?, ?, ?, ?)',
              (timestamp, username, 'face_recognition', status, ''))
    conn.commit()
    conn.close()

def main():
    known_encodings, known_names = load_model()
    if known_encodings is None:
        return
    
    print("Starting real-time face recognition...")
    print("Press 'q' to quit.\n")
    
    video_capture = cv2.VideoCapture(0)
    
    if not video_capture.isOpened():
        print("Error: Could not open webcam.")
        return
    
    process_this_frame = True
    last_logged = {}
    
    while True:
        ret, frame = video_capture.read()
        
        if not ret:
            print("Error: Could not read frame.")
            break
        
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        
        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            
            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_encodings, face_encoding)
                name = "Unknown"
                
                face_distances = face_recognition.face_distance(known_encodings, face_encoding)
                best_match_index = face_distances.argmin()
                
                if matches[best_match_index]:
                    name = known_names[best_match_index]
                
                face_names.append(name)
        
        process_this_frame = not process_this_frame
        
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            
            color = (0, 0, 255)
            if name != "Unknown":
                color = (0, 255, 0)
                
                now = datetime.datetime.now()
                if name not in last_logged or (now - last_logged[name]).total_seconds() > 10:
                    log_access(name, 'success')
                    last_logged[name] = now
                    print(f"Recognized: {name} at {now.strftime('%Y-%m-%d %H:%M:%S')}")
            else:
                now = datetime.datetime.now()
                if 'Unknown' not in last_logged or (now - last_logged['Unknown']).total_seconds() > 10:
                    log_access('Unknown', 'failed')
                    last_logged['Unknown'] = now
                    print(f"Unknown face detected at {now.strftime('%Y-%m-%d %H:%M:%S')}")
            
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), color, cv2.FILLED)
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.75, (255, 255, 255), 1)
        
        cv2.imshow('Face Recognition', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
