Code Generator: QR Codes and Barcodes

This Python script allows you to generate QR codes and barcodes from various types of data inputs. The script supports creating QR codes for URLs, numbers, WiFi connection details, CV links, and email addresses. Additionally, it can generate barcodes for any 12-digit number.

-Features:

QR Code Generation: Create QR codes that encode URLs, numbers, WiFi credentials, CV download links, and email addresses.
Barcode Generation: Produce EAN-13 barcodes for 12-digit numerical data.
Flexible Input Options: Choose the type of data to encode through command-line arguments.
Easy to Use: Simple CLI for generating the desired codes with minimal effort.
Prerequisites
Before you start using this script, make sure you have Python installed on your machine along with the necessary libraries. You can install the required libraries using pip:

Bash:
```
pip install qrcode[pil]
pip install python-barcode
```
-How to Use:
Clone the Repository: First, clone this repository to your local machine.
Install Dependencies: Run the commands listed above under Prerequisites to install necessary packages.
-Running the Script:
Open your terminal and navigate to the script's directory.
Use the following syntax to run the script:
Bash:
```
python code_generator.py [options]
```
Options:

-Q, --qr : Generate a QR code.
-B, --barcode : Generate a barcode.
-u, --url : Data type is a URL (for QR code).
-n, --number : Data type is a number (for QR code or barcode).
-w, --wifi : Data type is WiFi connection details (for QR code).
-c, --cv : Data type is a link to a CV (for QR code).
-e, --email : Data type is an email address (for QR code).

-Examples:

Generate a QR Code for a URL:

-Bash:
```
python code_generator.py -Q -u
```
After running the command, you will be prompted to enter the URL.

Generate a Barcode for a 12-digit Number:

-Bash:
```
python code_generator.py -B -n
```
You will be prompted to enter a 12-digit number.

-Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.
