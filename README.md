#  Smart Attendance System

A smart and secure attendance system that uses **QR code scanning and face recognition** to verify user identity.  
Built with a clean, interactive **Streamlit interface** for seamless user experience.

##  Current Features



-  Register user's face using webcam
-  Automatically generate and download a personal QR code
-  QR code + face verification for attendance
-  Records stored in Excel file
-  Fully interactive Streamlit web UI
-  Modular, clean, and reusable code




##  Face + QR Verification & Attendance Logging
verify user qr with corresponding face 

Run:

```bash
python face_recognition_app/verify_and_log.py

##  Streamlit -  Registration UI

Run the Streamlit app to register users and generate their QR codes.

```bash
streamlit run streamlit_app/registration_ui.py

1-User enters their name

2-Takes a picture using webcam

3-Face encoding saved under /encodings

4-QR code is auto-generated and displayed

5-Option to download the QR as PNG

##  Streamlite - Attendance Verification Page

Run the Streamlit app to  Attendance Verification Page with face and QR codes of Users.

```bash
streamlit run streamlit_app/attendance_ui.py

User scans their QR code using webcam

1-System extracts name from QR

2-Then asks for a face image to verify identity

3-If the face matches the registered encoding → attendance is recorded in attendance_log.xlsx

## 🛠 How to Run

# Install dependencies
install  requirements.txt

# Run face registration UI
streamlit run streamlit_app/face_registration_ui.py

# Run attendance verification UI
streamlit run streamlit_app/attendance_ui.py