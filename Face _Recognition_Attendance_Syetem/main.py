import cv2
import face_recognition
import pickle
import time
import csv
from datetime import datetime
import os

# Load encodings
with open("encodings.pickle", "rb") as f:
    data = pickle.load(f)

# Attendance file
attendance_file = "attendance.csv"
today = datetime.now().strftime("%Y-%m-%d")
existing_entries = set()

# Load existing attendance for today to avoid duplicates
if os.path.exists(attendance_file):
    with open(attendance_file, "r") as f:
        reader = csv.reader(f)
        next(reader, None)  # Skip header
        for row in reader:
            if len(row) >= 2:
                name, date = row[0], row[1]
                if date == today:
                    existing_entries.add(name)

# Start webcam
cap = cv2.VideoCapture(0)
print("\n✅ Webcam started. Press 'q' to quit.")

detected_names = []

while True:
    success, frame = cap.read()
    if not success:
        break

    # Resize for faster processing
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
        top, right, bottom, left = [v * 4 for v in location]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, f"{name} face detected", (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Check and record attendance
        if name != "Unknown" and name not in detected_names and name not in existing_entries:
            now = datetime.now()
            timestamp = now.strftime("%H:%M:%S")

            file_exists = os.path.isfile(attendance_file)
            with open(attendance_file, "a", newline="") as f:
                writer = csv.writer(f)
                if not file_exists:
                    writer.writerow(["Name", "Date", "Time"])
                writer.writerow([name, today, timestamp])

            print(f"✅ Success: {name} face detected successfully. Attendance Recorded!")
            detected_names.append(name)
            existing_entries.add(name)  # Add to today's log to prevent repeat

    cv2.imshow("Webcam Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
print("\n📷 Webcam feed ended.")
