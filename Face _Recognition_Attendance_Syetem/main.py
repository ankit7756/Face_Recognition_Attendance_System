import cv2
import face_recognition
import pickle
import time

# Load encodings
with open("encodings.pickle", "rb") as f:
    data = pickle.load(f)

# Start webcam
cap = cv2.VideoCapture(0)
print("\n✅ Webcam started. Running for 5 seconds...")

start_time = time.time()
detected_names = []

while True:
    success, frame = cap.read()
    if not success:
        break

    # Resize for faster processing (optional)
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Detect faces and encode
    face_locations = face_recognition.face_locations(rgb_small)
    face_encodings = face_recognition.face_encodings(rgb_small, face_locations)

    for encoding, location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(data["encodings"], encoding)
        name = "Unknown"

        if True in matches:
            match_index = matches.index(True)
            name = data["names"][match_index]

        # Draw box and label
        top, right, bottom, left = [v * 4 for v in location]  # scale back up
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, f"{name} face detected", (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Console log only once
        if name not in detected_names:
            print(f"Success: {name} face detected successfully. Attendance Recorded!")
            detected_names.append(name)

    cv2.imshow("Webcam Feed", frame)

    # Stop after 5 seconds or if 'q' is pressed
    if (time.time() - start_time > 1000) or (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
print("\n📷 Webcam feed ended.")
