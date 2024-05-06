import argparse
import sys
from urllib.parse import quote
import qrcode
from barcode import EAN13
from barcode.writer import ImageWriter

def generate_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_code_img.png")
    print("QR code generated and saved as qr_code_img.png")

def generate_barcode(data):
    if len(data) != 12:
        raise ValueError("Number for barcode must be 12 digits long.")
    barcode = EAN13(data, writer=ImageWriter())
    barcode.save("barcode")
    print("Barcode generated and saved as barcode.png")

def main():
    parser = argparse.ArgumentParser(description="Generate QR code or Barcode based on provided data.")
    parser.add_argument("-Q", "--qr", action="store_true", help="Generate QR code")
    parser.add_argument("-B", "--barcode", action="store_true", help="Generate Barcode")
    parser.add_argument("-u", "--url", action="store_true", help="Generate code for a URL")
    parser.add_argument("-n", "--number", action="store_true", help="Generate code for a number")
    parser.add_argument("-w", "--wifi", action="store_true", help="Generate code for a WiFi connection")
    parser.add_argument("-c", "--cv", action="store_true", help="Generate code for downloading a CV")
    parser.add_argument("-e", "--email", action="store_true", help="Generate code for an email address")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        print("No valid arguments provided.")
        return

    data_type = None
    if args.url:
        data_type = 'Please type the URL Address: '
    elif args.number:
        data_type = 'Please type the number: '
    elif args.wifi:
        data_type = 'Please type the WiFi SSID, Password, Encryption (e.g., WPA): '
    elif args.cv:
        data_type = 'Please type the Link for CV: '
    elif args.email:
        data_type = 'Please type the Email Address: '
    
    if data_type:
        input_data = input(f"Enter {data_type}")
        if args.cv:
            input_data = "Download my CV at: " + input_data
        if args.wifi:
            ssid, password, encryption = input_data.split(',')
            input_data = f"WIFI:S:{ssid};T:{encryption};P:{password};;"
        if args.url:
            input_data = quote(input_data)
    else:
        print("No valid data type argument provided.")
        return

    if args.qr:
        generate_qr(input_data)
    elif args.barcode:
        generate_barcode(input_data)
    else:
        print("Specify either QR code (-Q) or Barcode (-B) generation.")

if __name__ == "__main__":
    main()
