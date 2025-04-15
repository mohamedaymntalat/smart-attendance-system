import cv2
import face_recognition
import pickle
import os
from pyzbar.pyzbar import decode
from datetime import datetime
import pandas as pd

#  Load known face encoding
def load_encoding(name, encoding_dir="face_recognition_app/encodings"):
    file_path = os.path.join(encoding_dir, f"{name.lower().replace(' ', '_')}.pkl")
    if not os.path.exists(file_path):
        print(f"[X] No encoding found for user: {name}")
        return None
    with open(file_path, "rb") as f:
        return pickle.load(f)

#  Save attendance to Excel
def log_attendance(name, log_file="attendance_log.xlsx"):
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {'Name': [name], 'Timestamp': [time_now]}

    if not os.path.exists(log_file):
        df = pd.DataFrame(data)
    else:
        df_existing = pd.read_excel(log_file, engine='openpyxl')
        df_new = pd.DataFrame(data)
        df = pd.concat([df_existing, df_new], ignore_index=True)

    df.to_excel(log_file, index=False)
    print(f"[✔] Logged attendance for: {name} at {time_now}")

#  Main face verification + QR reading
def verify_attendance():
    cap = cv2.VideoCapture(0)
    print("[INFO] Starting camera. Show your QR code...")

    user_name = None
    known_encoding = None
    verified = False

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        # Show frame
        cv2.imshow("QR + Face Verification", frame)

        # 1. Try to read QR code
        qr_codes = decode(frame)
        if qr_codes and user_name is None:
            qr_data = qr_codes[0].data.decode("utf-8")
            user_name = qr_data.split("|")[0]
            print(f"[INFO] QR code detected: {user_name}")

            known_encoding = load_encoding(user_name)
            if known_encoding is None:
                break

        # 2. If QR found, try to verify face
        if user_name and known_encoding is not None:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(rgb_frame)
            if len(face_locations) == 1:
                face_encoding = face_recognition.face_encodings(rgb_frame, face_locations)[0]

                # Compare faces
                result = face_recognition.compare_faces([known_encoding], face_encoding, tolerance=0.5)
                if result[0]:
                    log_attendance(user_name)
                    verified = True
                    print(f"[✔] Face verified for {user_name}")
                    break
                else:
                    print("[X] Face does not match QR user.")

        key = cv2.waitKey(1)
        if key == ord('q') or verified:
            break

    cap.release()
    cv2.destroyAllWindows()

# Run
if __name__ == "__main__":
    verify_attendance()
