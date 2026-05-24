import os
import pickle
import datetime
import sqlite3

DATASET_DIR = 'dataset'
MODELS_DIR = 'models'
DATABASE = 'database.db'

def mock_train():
    print("=" * 50)
    print("🧪 Mock Model Training (Testing Mode)")
    print("=" * 50)
    
    known_encodings = []
    known_names = []
    
    if not os.path.exists(DATASET_DIR):
        print("❌ Dataset directory not found!")
        return False
    
    dataset_people = [d for d in os.listdir(DATASET_DIR) if os.path.isdir(os.path.join(DATASET_DIR, d))]
    if not dataset_people:
        print("❌ No people folders found in dataset!")
        return False
    
    total_photos = 0
    for person_name in dataset_people:
        person_dir = os.path.join(DATASET_DIR, person_name)
        photos = [f for f in os.listdir(person_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        total_photos += len(photos)
        print(f"👤 Found {len(photos)} photos for '{person_name}'")
        
        for i in range(len(photos)):
            mock_encoding = [float(hash(f"{person_name}_{i}") % 1000) / 100 for _ in range(128)]
            known_encodings.append(mock_encoding)
            known_names.append(person_name)
    
    if total_photos == 0:
        print("❌ No photos found!")
        return False
    
    if not os.path.exists(MODELS_DIR):
        os.makedirs(MODELS_DIR)
    
    model_data = {
        'encodings': known_encodings,
        'names': known_names
    }
    
    model_path = os.path.join(MODELS_DIR, 'face_model.pkl')
    with open(model_path, 'wb') as f:
        pickle.dump(model_data, f)
    
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('INSERT INTO access_logs (timestamp, username, action, status, details) VALUES (?, ?, ?, ?, ?)',
              (timestamp, 'system', 'mock_train_model', 'success', 
               f'Mock trained on {len(known_encodings)} faces from {len(set(known_names))} people'))
    conn.commit()
    conn.close()
    
    print("\n✅ Mock Training Complete!")
    print(f"   - {len(known_encodings)} faces encoded")
    print(f"   - {len(set(known_names))} people recognized")
    print(f"   - Model saved to {model_path}")
    print("=" * 50)
    
    return True

if __name__ == "__main__":
    mock_train()
