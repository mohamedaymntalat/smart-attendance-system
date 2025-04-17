import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

import streamlit as st
from qr_generator.generate_qr import generate_qr_code
from face_recognition_app.register_face import register_face



def main():
    st.set_page_config(page_title="نظام تسجيل الوجه + QR", layout="centered")
    st.title("📌 نظام تسجيل الوجه + QR")

    # Input: user name
    user_name = st.text_input("🧑 الاسم الكامل")

    # Capture face image in-browser
    image_file = st.camera_input("📷 التقط صورة وجهك")

    # Trigger registration
    if st.button("ابدأ التسجيل"):
        if not user_name.strip():
            st.warning("الاسم لا يمكن أن يكون فارغًا.")
        elif image_file is None:
            st.warning("الرجاء التقاط صورة وجهك أولاً.")
        else:
            success, encoding_path, face_count = register_face(image_file, user_name)

            if not success:
                if face_count == 0:
                    st.error("❌ لم يتم الكشف عن أي وجه. حاول مرة أخرى.")
                else:
                    st.error("❌ تم الكشف عن أكثر من وجه. الرجاء إظهار وجه واحد فقط.")
            else:
                st.success(f"✅ تم تسجيل وجه المستخدم ({user_name})")

                # Generate QR code and display
                file_path, buffer = generate_qr_code(user_name, return_bytes=True)
                st.image(buffer, caption="🎯 هذا هو QR الخاص بك")

                # Download button for QR
                st.download_button(
                    label="⬇️ تحميل QR كود",
                    data=buffer,
                    file_name=f"{user_name.replace(' ', '_')}_qr.png",
                    mime="image/png"
                )

if __name__ == "__main__":
    main()
