import os
import pickle
import numpy as np
from collections import Counter, defaultdict

def load_model():
    model_path = os.path.join('models', 'face_model.pkl')
    if not os.path.exists(model_path):
        print("Model not found! Please train the model first.")
        return None, None
    
    with open(model_path, 'rb') as f:
        data = pickle.load(f)
    
    return data['encodings'], data['names']

def check_accuracy():
    try:
        import face_recognition
    except ImportError:
        print("=" * 70)
        print("⚠️  DEPENDENCY MISSING")
        print("=" * 70)
        print("\nPlease install face_recognition_models first:")
        print("\n  pip install git+https://github.com/ageitgey/face_recognition_models")
        print("\nOr if you have issues, you can use the web interface instead!")
        print("=" * 70)
        return 0
    
    dataset_dir = 'dataset'
    
    if not os.path.exists(dataset_dir):
        print("Dataset directory not found!")
        return
    
    known_encodings, known_names = load_model()
    if known_encodings is None:
        return
    
    print("=" * 70)
    print("FACE RECOGNITION ACCURACY CHECK")
    print("=" * 70)
    
    total_tested = 0
    correct = 0
    person_results = defaultdict(lambda: {'total': 0, 'correct': 0})
    
    print("\nTesting each photo in the dataset...")
    print("-" * 70)
    
    for person_name in os.listdir(dataset_dir):
        person_dir = os.path.join(dataset_dir, person_name)
        
        if not os.path.isdir(person_dir):
            continue
        
        print(f"\nTesting: {person_name}")
        
        for image_file in os.listdir(person_dir):
            if not image_file.lower().endswith(('.jpg', '.jpeg', '.png')):
                continue
            
            image_path = os.path.join(person_dir, image_file)
            
            try:
                image = face_recognition.load_image_file(image_path)
                encodings = face_recognition.face_encodings(image)
                
                if encodings:
                    test_encoding = encodings[0]
                    
                    matches = face_recognition.compare_faces(known_encodings, test_encoding)
                    face_distances = face_recognition.face_distance(known_encodings, test_encoding)
                    
                    if len(face_distances) > 0:
                        best_match_index = np.argmin(face_distances)
                        predicted_name = known_names[best_match_index] if matches[best_match_index] else "Unknown"
                        
                        total_tested += 1
                        person_results[person_name]['total'] += 1
                        
                        if predicted_name == person_name:
                            correct += 1
                            person_results[person_name]['correct'] += 1
                            print(f"  OK {image_file}: CORRECT")
                        else:
                            print(f"  XX {image_file}: WRONG - predicted '{predicted_name}'")
                    
            except Exception as e:
                print(f"  -- {image_file}: Error")
    
    print("\n" + "=" * 70)
    print("FINAL RESULTS")
    print("=" * 70)
    
    if total_tested > 0:
        overall_accuracy = (correct / total_tested) * 100
        print(f"\nOverall Accuracy: {correct}/{total_tested} ({overall_accuracy:.1f}%)")
        
        print("\nAccuracy by Person:")
        print("-" * 40)
        for name in sorted(person_results.keys()):
            res = person_results[name]
            if res['total'] > 0:
                acc = (res['correct'] / res['total']) * 100
                print(f"  {name:20s} {res['correct']}/{res['total']:3d}  ({acc:5.1f}%)")
    
    print("\n" + "=" * 70)
    print("\nTips to improve accuracy:")
    print("• Add more photos (5+ recommended per person)")
    print("• Use photos from different angles and lighting")
    print("• Ensure faces are clear and well-lit")
    print("• Remove photos with blurry faces or obstructions")
    
    return overall_accuracy if total_tested > 0 else 0

if __name__ == "__main__":
    check_accuracy()
