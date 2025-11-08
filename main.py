#!/usr/bin/env python3
import argparse
import qrcode
from PIL import Image

def generate_qr_with_logo(data, logo_path, output_path, box_size=10):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    if logo_path:
        logo = Image.open(logo_path).convert("RGBA")

        # Resize logo
        qr_width, qr_height = qr_img.size
        logo_size = qr_width // 4
        orig_w, orig_h = logo.size
        ratio = min(logo_size / orig_w, logo_size / orig_h)

        new_size = (int(orig_w * ratio), int(orig_h * ratio))
        logo = logo.resize(new_size, Image.LANCZOS)

        # Paste logo
        pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
        qr_img.paste(logo, pos, mask=logo)  # 使用 alpha channel 當遮罩

    qr_img.save(output_path)
    print(f"✅ Saved QR Code to: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Generate QR code with optional center logo")
    parser.add_argument("-d", "--data", required=True, help="Data or URL to encode in the QR code")
    parser.add_argument("-l", "--logo", help="Path to logo image (optional)")
    parser.add_argument("-o", "--output", default="qr.png", help="Output filename")
    parser.add_argument("-s", "--scale", type=int, default=10, help="Box size (default: 10)")

    args = parser.parse_args()
    generate_qr_with_logo(args.data, args.logo, args.output, box_size=args.scale)

if __name__ == "__main__":
    main()
