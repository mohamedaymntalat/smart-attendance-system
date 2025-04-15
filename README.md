#  Smart Attendance System

This is a smart attendance system using QR codes and face recognition.

##  Current Features

- Generate QR codes for users based on their names
- Each QR code embeds user name and date
- Saved as PNG in `qr_codes/` folder

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
