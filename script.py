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
