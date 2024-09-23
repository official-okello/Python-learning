import qrcode

text = input("Enter text or URL: ").strip()
file = input("Enter filename: ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(text)
qr_code_image = qr.make_image(fill_color="black", back_color="white")
qr_code_image.save(file)

print(f"QR code saved as {file}")