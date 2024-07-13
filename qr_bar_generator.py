import argparse
import sys
from urllib.parse import urlparse, urlunparse
import qrcode
from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw


def generate_qr(data, logo_path=None):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Use high error correction for better embedding
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

    if logo_path:
        try:
            logo = Image.open(logo_path)

            # Calculate the logo size and position
            base_width = img.size[0]
            logo_size = int(base_width / 4)
            logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

            # Create a transparent box in the center
            logo_position = (
                (img.size[0] - logo_size) // 2,
                (img.size[1] - logo_size) // 2,
            )
            transparent_area = Image.new('RGBA', img.size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(transparent_area)
            draw.rectangle(
                [logo_position, (logo_position[0] + logo_size, logo_position[1] + logo_size)],
                fill=(255, 255, 255, 255)
            )

            combined = Image.alpha_composite(img, transparent_area)
            combined.paste(logo, logo_position, logo)
            img = combined
        except Exception as e:
            print(f"An error occurred while processing the logo image: {e}")
            return

    img.save("qr_code_img.png")
    print("QR code generated and saved as qr_code_img.png")


def generate_barcode(data):
    if len(data) != 12:
        raise ValueError("Number for barcode must be 12 digits long.")
    barcode = EAN13(data, writer=ImageWriter())
    barcode.save("barcode")
    print("Barcode generated and saved as barcode.png")


def ensure_url_has_scheme(url):
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        return urlunparse(parsed_url._replace(scheme="http"))
    return url


def main():
    parser = argparse.ArgumentParser(description="Generate QR code or Barcode based on provided data.")
    parser.add_argument("-Q", "--qr", action="store_true", help="Generate QR code")
    parser.add_argument("-B", "--barcode", action="store_true", help="Generate Barcode")
    parser.add_argument("data", type=str, help="The data for the QR code or Barcode (URL or number)")
    parser.add_argument("-u", "--url", action="store_true", help="Indicate the data is a URL")
    parser.add_argument("-n", "--number", action="store_true", help="Indicate the data is a number")
    parser.add_argument("-w", "--wifi", action="store_true", help="Indicate the data is WiFi configuration (SSID,Password,Encryption)")
    parser.add_argument("-c", "--cv", action="store_true", help="Indicate the data is a CV download link")
    parser.add_argument("-e", "--email", action="store_true", help="Indicate the data is an email address")
    parser.add_argument("-i", "--image", type=str, help="Path to an image file to embed in the QR code")
    args = parser.parse_args()

    input_data = args.data

    if args.cv:
        input_data = "Download my CV at: " + input_data
    elif args.wifi:
        ssid, password, encryption = input_data.split(',')
        input_data = f"WIFI:S:{ssid};T:{encryption};P:{password};;"
    elif args.url:
        input_data = ensure_url_has_scheme(input_data)

    if args.qr:
        generate_qr(input_data, args.image)
    elif args.barcode:
        if not args.number:
            print("Barcode can only be generated for numbers. Please use -n flag.")
            return
        generate_barcode(input_data)
    else:
        print("Specify either QR code (-Q) or Barcode (-B) generation.")


if __name__ == "__main__":
    main()
