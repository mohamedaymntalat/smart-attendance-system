import qrcode
from PIL import Image
from io import BytesIO
import os
from datetime import datetime

def generate_qr_code(user_name, output_dir="qr_generator/qr_codes", return_bytes=False):
    os.makedirs(output_dir, exist_ok=True)
    qr_data = f"{user_name}|{datetime.now().strftime('%Y-%m-%d')}"

    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(qr_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    file_path = os.path.join(output_dir, f"{user_name.lower().replace(' ', '_')}_qr.png")
    img.save(file_path)

    if return_bytes:
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        return file_path, buffer

    return file_path, None
