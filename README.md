
**README.md**
```md
# QR Code Generator

A simple Python script to generate QR codes with customizable colors and border sizes.

## Features
- Generate QR codes from text or URLs
- Customize fill and background colors
- Adjust border size
- Save QR codes as `.png`, `.jpg`, or `.jpeg`

## Requirements
- Python 3.x
- `qrcode[pil]`

## Installation
```sh
pip install -r requirements.txt
```

## Usage
```sh
python main.py
```
Follow the prompts to enter QR code details.

## Example
```sh
Enter text or URL for the QR code: https://www.example.com
Enter fill color (default: '#000000'): white
Enter background color (default: '#FFFFFF'): white
Enter border size (default: 1): 2
Enter the directory to save the QR code (e.g., /path/to/folder): ./output
Enter the filename to save the QR code (e.g., output.png): example_qr
```

![image](https://github.com/user-attachments/assets/b89b2048-be1c-4467-b11b-7f1adcacd761)




The QR code will be saved as `./output/example_qr.png`.
