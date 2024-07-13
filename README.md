# Qr bar generator: QR Codes and Barcodes

This Python script allows you to generate QR codes and barcodes from various types of data inputs. The script supports creating QR codes for URLs, numbers, WiFi connection details, CV links, and email addresses. Additionally, it can generate barcodes for any 12-digit number. It also supports embedding a logo into the center of a QR code.

## Features:

- **QR Code Generation**: Create QR codes that encode URLs, numbers, WiFi credentials, CV download links, and email addresses.
- **Barcode Generation**: Produce EAN-13 barcodes for 12-digit numerical data.
- **Embed Logo in QR Code**: Optionally embed a logo in the center of the generated QR code.
- **Flexible Input Options**: Choose the type of data to encode through command-line arguments.
- **Easy to Use**: Simple CLI for generating the desired codes with minimal effort.
- **URL Normalization**: Automatically adds the HTTP scheme to URLs if missing.

## Prerequisites

Before you start using this script, make sure you have Python installed on your machine along with the necessary libraries. You can install the required libraries using pip:

```bash
pip install qrcode[pil] python-barcode pillow
```
## How to Use:

1. **Clone the Repository**: First, clone this repository to your local machine.

2. **Install Dependencies**: Run the commands listed above under Prerequisites to install necessary packages.

3. **Running the Script**: Open your terminal, navigate to the script's directory, and use the following syntax to run the script:

```bash
python qr_bar_generator.py [options]

python qr_bar_generator.py [options]
```
## Options:

```bash
-Q, --qr         Generate a QR code.
-B, --barcode    Generate a barcode.
-u, --url        Specify that the data is a URL (for QR code).
-n, --number     Specify that the data is a number (for QR code or barcode).
-w, --wifi       Specify that the data is WiFi connection details (for QR code).
-c, --cv         Specify that the data is a link to a CV (for QR code).
-e, --email      Specify that the data is an email address (for QR code).
-i, --image      Path to an image file to embed in the QR code.
```
## Examples:

Generate a QR Code for a URL:

-Bash:
```
python qr_bar_generator.py -Q -u -i "path_of_the_image"
```
After running the command, you will be prompted to enter the URL.

Generate a Barcode for a 12-digit Number:

-Bash:
```
python qr_bar_generator.py -B -n
```
You will be prompted to enter a 12-digit number.

## Contributions

-Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.
