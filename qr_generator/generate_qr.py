import qrcode
#from PIL import Image
import os
from datetime import datetime


# Function to generate QR code based on user name
def generate_qr_code(user_name, output_dir="qr_codes"):

    #Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    #Create the QR data (could be more complex, like JSON or user ID)
    qr_data = f"{user_name}|{datetime.now().strftime('%Y-%m-%d')}"

    #Create QR code object
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    #Add data to QR and generate it
    qr.add_data(qr_data)
    qr.make(fit=True)

    #Create the image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    #Define the path and save the image
    filename = f"{user_name.replace(' ', '_')}_qr.png"
    file_path = os.path.join(output_dir, filename)
    img.save(file_path)

    print(f"[✔] QR code generated and saved at: {file_path}")
    return file_path

#Example Usage
if __name__ == "__main__":
    name = input("Enter your name to generate QR code: ")
    generate_qr_code(name)
