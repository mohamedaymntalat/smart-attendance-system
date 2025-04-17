# streamlit_app/attendance_ui.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import face_recognition
import pickle
from pyzbar.pyzbar import decode
import numpy as np
from PIL import Image
from datetime import datetime
import pandas as pd

ENCODING_DIR = "face_recognition_app/encodings"
LOG_FILE = "attendance_log.xlsx"

# ======================================
# 🧠 Load face encoding for a given name
# ======================================
def load_encoding(user_name):
    filename = f"{user_name.lower().replace(' ', '_')}.pkl"
    path = os.path.join(ENCODING_DIR, filename)
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        return pickle.load(f)

# ======================================
# ✍️ Log attendance to Excel file
# ======================================
def log_attendance(name):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_entry = pd.DataFrame({'Name': [name], 'Timestamp': [timestamp]})

    if os.path.exists(LOG_FILE):
        df = pd.read_excel(LOG_FILE)
        df = pd.concat([df, new_entry], ignore_index=True)
    else:
        df = new_entry

    df.to_excel(LOG_FILE, index=False)

# ======================================
# 🎯 Streamlit Attendance Page
# ======================================
def main():
    st.set_page_config(page_title="تسجيل الحضور", layout="centered")
    st.title("✅ تسجيل الحضور باستخدام QR + الوجه")

    st.write("1️⃣ امسح QR الكود الخاص بك")
    qr_image = st.camera_input("📷 التقط صورة لــ QR")

    if qr_image:
        qr_pil = Image.open(qr_image)
        frame = np.array(qr_pil.convert("RGB"))
        qr_codes = decode(frame)

        if not qr_codes:
            st.error("❌ لم يتم العثور على QR كود. تأكد من وضوح الصورة.")
            return

        # قراءة الاسم من QR
        qr_data = qr_codes[0].data.decode("utf-8")
        user_name = qr_data.split("|")[0].strip()
        st.success(f"✅ تم التعرف على المستخدم: {user_name}")

        # تحميل الـ face encoding
        encoding = load_encoding(user_name)
        if encoding is None:
            st.error("⚠️ لم يتم العثور على بيانات الوجه لهذا المستخدم.")
            return

        st.divider()
        st.write("2️⃣ التقط صورة لوجهك للتحقق")

        face_image = st.camera_input("📷 التقط صورة وجهك")

        if face_image:
            face_pil = Image.open(face_image)
            rgb = np.array(face_pil.convert("RGB"))
            face_locations = face_recognition.face_locations(rgb)

            if len(face_locations) != 1:
                st.warning("⛔ تأكد من أن وجه واحد فقط ظاهر في الصورة.")
                return

            face_encoding = face_recognition.face_encodings(rgb, face_locations)[0]
            result = face_recognition.compare_faces([encoding], face_encoding, tolerance=0.5)

            if result[0]:
                log_attendance(user_name)
                st.success(f"✅ تم تسجيل حضور {user_name} بنجاح 🎉")
            else:
                st.error("❌ الوجه لا يطابق الاسم الموجود في QR")

if __name__ == "__main__":
    main()

