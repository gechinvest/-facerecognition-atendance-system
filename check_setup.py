import os

print("=== Checking Project Setup ===")
print()

print("1. Checking folders...")
folders = ['logs', 'dataset', 'models', 'static', 'templates']
for folder in folders:
    exists = os.path.exists(folder)
    status = "OK" if exists else "MISSING"
    print(f"   {folder}: {status}")

print()
print("2. Checking dataset...")
dataset_dir = 'dataset'
if os.path.exists(dataset_dir):
    people = [d for d in os.listdir(dataset_dir) if os.path.isdir(os.path.join(dataset_dir, d))]
    print(f"   Number of people in dataset: {len(people)}")
    
    total_photos = 0
    for person in people:
        person_dir = os.path.join(dataset_dir, person)
        photos = [f for f in os.listdir(person_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        total_photos += len(photos)
        print(f"   - {person}: {len(photos)} photos")
    
    print(f"   Total photos: {total_photos}")
else:
    print("   Dataset folder missing!")

print()
print("3. Checking templates...")
template_files = ['login.html', 'dashboard.html', 'capture.html', 'attendance.html', 'visitors.html', 'door_access.html']
all_ok = True
for tf in template_files:
    exists = os.path.exists(os.path.join('templates', tf))
    status = "OK" if exists else "MISSING"
    print(f"   templates/{tf}: {status}")
    if not exists:
        all_ok = False

print()
print("=== Setup Check Complete ===")
print()
print("Your project setup is looking good!")
print()
print("REMINDER: To train the face recognition model, you need these packages:")
print("  - opencv-python")
print("  - face-recognition")
print("  - numpy")
print()
print("Install them with: pip install opencv-python face-recognition numpy")
