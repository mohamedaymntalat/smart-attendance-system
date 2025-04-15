import cv2
import face_recognition
import pickle
import os

# Function to register a new user's face
def register_user(name, save_dir="face_recognition_app/encodings"):

    #Create encoding directory if not exists
    os.makedirs(save_dir, exist_ok=True)

    # Start webcam
    cap = cv2.VideoCapture(0)
    print("[INFO] Starting camera... Press 's' to capture your face.")

    face_encoding = None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Failed to grab frame.")
            break

        #Display the frame
        cv2.imshow("Face Registration - Press 's' to capture", frame)

        #Wait for key press
        key = cv2.waitKey(1) & 0xFF

        #If 's' is pressed → capture frame
        if key == ord("s"):
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            #Detect face & encode
            face_locations = face_recognition.face_locations(rgb_frame)
            if len(face_locations) != 1:
                print("[WARNING] Please ensure one face is visible.")
                continue

            face_encoding = face_recognition.face_encodings(rgb_frame, face_locations)[0]
            break

        elif key == ord("q"):
            print("[INFO] Exiting without saving.")
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

    if face_encoding is not None:
        # Save encoding to file
        file_path = os.path.join(save_dir, f"{name.replace(' ', '_').lower()}.pkl")
        with open(file_path, "wb") as f:
            pickle.dump(face_encoding, f)

        print(f"[✔] Face encoding saved for user: {name} → {file_path}")
    else:
        print("[X] No encoding was saved.")

#  Example usage
if __name__ == "__main__":
    username = input("Enter your name to register face: ")
    register_user(username)
