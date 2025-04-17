import face_recognition
import pickle
import os
import numpy as np
from PIL import Image


def register_face(image_file, user_name, save_dir="face_recognition_app/encodings"):

    os.makedirs(save_dir, exist_ok=True)

    # Load image and convert to RGB numpy array
    img = Image.open(image_file)
    rgb = np.array(img.convert("RGB"))

    # Detect faces
    faces = face_recognition.face_locations(rgb)
    face_count = len(faces)

    # Must detect exactly one face
    if face_count != 1:
        return False, None, face_count

    # Compute encoding
    encoding = face_recognition.face_encodings(rgb, faces)[0]

    # Save encoding to disk
    filename = f"{user_name.lower().replace(' ', '_')}.pkl"
    file_path = os.path.join(save_dir, filename)
    with open(file_path, "wb") as f:
        pickle.dump(encoding, f)

    return True, file_path, face_count