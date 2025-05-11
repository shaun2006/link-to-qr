# link-to-qr
This is an simple python script to generate qr corde as image file from a link

This Python script generates a QR code based on a user-provided URL and saves it as a PNG file. The filename is generated based on the current timestamp in the format `YYYY-MM-DD_HH-MM-SS.png`.

## Prerequisites

* Python 3.x
* `qrcode` library

Install the required library using:

```bash
pip install qrcode[pil]
```

## How to Use

1. Run the script using the command:

```bash
python qr_code_generator.py
```

2. Enter the URL when prompted.

3. The QR code will be saved in the current directory with a filename based on the current timestamp.

Example filename: `2025-05-11_13-30-45.png`

## Example Usage

```
Please enter the link of the website: https://example.com
QR code saved as '2025-05-11_13-30-45.png'
```

###
![screenshort](https://github.com/shaun2006/link-to-qr/blob/main/linktoqrss.png?raw=true)


## Notes

* The timestamp in the filename ensures that each QR code has a unique name and avoids overwriting existing files.
* The script uses GMT time for filename generation. Adjust as necessary for your timezone.
