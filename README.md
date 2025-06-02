# 📱🔳 link-to-qr
This is an simple python script to generate qr corde as image file from a link

## 📌 Description
This Python script generates a QR code based on a user-provided URL and saves it as a PNG file. The filename is generated based on the current timestamp in the format `YYYY-MM-DD_HH-MM-SS.png`.

## ⚙️ Prerequisites

* Python 3.x
* `qrcode` library

Install the required library using:

```bash
pip install qrcode
```

## 🛠️ How to Use

1. Run the script using the command:

```bash
git clone https://github.com/shaun2006/link-to-qr.git
cd link-to-qr
python script.py
```

2. Enter the URL when prompted.

3. The QR code will be saved in the current directory with a filename based on the current timestamp.

Example filename: `2025-06-02_10-27-35.png`

## Example Usage

```
Please enter the link of the website: https://example.com
QR code saved as '2025-05-11_13-30-45.png'
```
### Output:- 
![](https://raw.githubusercontent.com/shaun2006/link-to-qr/refs/heads/main/2025-06-02_22-28.png?raw=true)

## 📂 Files

- `script.py` - all the code is in this file
- `2025-05-11_13-30-45.png` - the qr code 

## 👩‍💻 The code
``` python
import qrcode
from time import gmtime, strftime

# Create PNG QR Code
link = input("Please enter the link of the website: ")
img = qrcode.make(link)

# Replace ':' with '-' in the filename
name_of_image = strftime("%Y-%m-%d_%H-%M-%S", gmtime())

filename = name_of_image + '.png'

with open(filename, 'wb') as qr:
    img.save(qr)

print(f"QR code saved as '{filename}'")
```
### ScreenShorts of code
![screenshort](https://github.com/shaun2006/link-to-qr/blob/main/linktoqrss.png?raw=true)


## Notes

* The timestamp in the filename ensures that each QR code has a unique name and avoids overwriting existing files.

