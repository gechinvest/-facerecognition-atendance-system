import face_recognition
import os
import pickle
import numpy as np

def main():
    dataset_dir = 'dataset'
    models_dir = 'models'
    
    if not os.path.exists(dataset_dir):
        print(f"Error: Dataset directory '{dataset_dir}' not found!")
        return
    
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)
    
    known_encodings = []
    known_names = []
    
    print("Starting face encoding...")
    
    for person_name in os.listdir(dataset_dir):
        person_dir = os.path.join(dataset_dir, person_name)
        
        if not os.path.isdir(person_dir):
            continue
        
        print(f"Processing {person_name}...")
        
        for image_file in os.listdir(person_dir):
            if image_file.lower().endswith(('.jpg', '.jpeg', '.png')):
                image_path = os.path.join(person_dir, image_file)
                
                try:
                    image = face_recognition.load_image_file(image_path)
                    encodings = face_recognition.face_encodings(image)
                    
                    if encodings:
                        known_encodings.append(encodings[0])
                        known_names.append(person_name)
                        print(f"  Encoded: {image_file}")
                    else:
                        print(f"  No face found in: {image_file}")
                        
                except Exception as e:
                    print(f"  Error processing {image_file}: {e}")
    
    if known_encodings:
        model_data = {
            'encodings': known_encodings,
            'names': known_names
        }
        
        model_path = os.path.join(models_dir, 'face_model.pkl')
        with open(model_path, 'wb') as f:
            pickle.dump(model_data, f)
        
        print(f"\nTraining complete!")
        print(f"Total faces encoded: {len(known_encodings)}")
        print(f"Model saved to: {model_path}")
    else:
        print("\nNo faces were encoded. Please add images to the dataset folder.")

if __name__ == "__main__":
    main()
