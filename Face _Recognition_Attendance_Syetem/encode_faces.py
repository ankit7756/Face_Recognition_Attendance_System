import os
import cv2
import face_recognition
import pickle

# Path to images folder
IMAGE_PATH = 'Images'
known_encodings = []
known_names = []

# Loop through each image
for filename in os.listdir(IMAGE_PATH):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(IMAGE_PATH, filename)
        image = cv2.imread(img_path)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Get encodings
        encodings = face_recognition.face_encodings(rgb)

        if encodings:
            known_encodings.append(encodings[0])
            name = os.path.splitext(filename)[0]
            known_names.append(name)
            print(f"[INFO] Processed {filename}")
        else:
            print(f"[WARNING] No face found in {filename}")

# Save encodings to file
data = {"encodings": known_encodings, "names": known_names}
with open("encodings.pickle", "wb") as f:
    pickle.dump(data, f)

print("\n✅ Face encoding completed and saved to encodings.pickle")
