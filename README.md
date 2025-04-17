#  Smart Attendance System

This is a smart attendance system using QR codes and face recognition.

##  Current Features

- Generate QR codes for users based on their names
- Each QR code embeds user name and date
- Saved as PNG in `qr_codes/` folder
- Take and save user face in .pkl file 'encodings/'folder
- Reads QR code from webcam
- Matches live face with registered encoding
- Logs attendance with name + timestamp in Excel file

##  Module: QR Generator

Path: `qr_generator/generate_qr.py`

To run:

```bash
python qr_generator/generate_qr.py

##  Face Registration

Allows users to register their face for future attendance verification.

Run:

```bash
python face_recognition_app/register_face.py

##  Face + QR Verification & Attendance Logging
verify user qr with corresponding face 

Run:

```bash
python face_recognition_app/verify_and_log.py

##  Streamlit -  Registration UI

Run the Streamlit app to register users and generate their QR codes.

```bash
streamlit run streamlit_app/registration_ui.py
