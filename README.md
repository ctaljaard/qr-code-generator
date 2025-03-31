{\rtf1\ansi\ansicpg1252\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 **README.md**\
```md\
# QR Code Generator\
\
A simple Python script to generate QR codes with customizable colors and border sizes.\
\
## Features\
- Generate QR codes from text or URLs\
- Customize fill and background colors\
- Adjust border size\
- Save QR codes as `.png`, `.jpg`, or `.jpeg`\
\
## Requirements\
- Python 3.x\
- `qrcode[pil]`\
\
## Installation\
```sh\
pip install -r requirements.txt\
```\
\
## Usage\
```sh\
python main.py\
```\
Follow the prompts to enter QR code details.\
\
## Example\
```sh\
Enter text or URL for the QR code: https://www.example.com\
Enter fill color (default: '#000000'): #FF5733\
Enter background color (default: '#FFFFFF'): white\
Enter border size (default: 1): 2\
Enter the directory to save the QR code (e.g., /path/to/folder): ./output\
Enter the filename to save the QR code (e.g., output.png): example_qr\
```\
The QR code will be saved as `./output/example_qr.png`.\
```\
\
**requirements.txt**\
```txt\
qrcode[pil]\
```\
}