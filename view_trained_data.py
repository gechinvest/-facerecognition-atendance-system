import pickle
import os
from collections import Counter

def view_trained_data():
    model_path = os.path.join('models', 'face_model.pkl')
    
    if not os.path.exists(model_path):
        print("Model file not found: {}".format(model_path))
        print("Please train the model first by visiting the 'Capture & Train' page in the app.")
        return
    
    try:
        with open(model_path, 'rb') as f:
            model_data = pickle.load(f)
        
        encodings = model_data.get('encodings', [])
        names = model_data.get('names', [])
        
        print("=" * 60)
        print("TRAINED FACE DATA SUMMARY")
        print("=" * 60)
        print("\nTotal faces trained: {}".format(len(encodings)))
        
        if len(encodings) == 0:
            print("No trained faces found.")
            return
        
        name_counts = Counter(names)
        unique_names = sorted(name_counts.keys())
        
        print("\nUnique people trained: {}".format(len(unique_names)))
        print("\nDetails by person:")
        print("-" * 40)
        for name in sorted(unique_names):
            count = name_counts[name]
            print("  - {}: {} photo{}".format(name, count, 's' if count != 1 else ''))
        
        print("\n" + "=" * 60)
        print("Training Tips:")
        print("  - Each person has 5+ photos recommended")
        print("  - More photos = better recognition accuracy")
        print("=" * 60)
        
    except Exception as e:
        print("Error loading model: {}".format(e))

if __name__ == "__main__":
    view_trained_data()
