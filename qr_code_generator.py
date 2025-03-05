import qrcode

def qr_data():
    data = input("Enter the text or URL: ").strip()
    return data

def file_name():
    filename = input("Enter the filename: ").strip()
    return filename

def save_image(img, filename):
    type(img)  # qrcode.image.pil.PilImage

    img.save(filename)
    print(f"QR code saved as {filename}")

def simple_qr_generator():
    data = qr_data()
    filename = file_name()

    img = qrcode.make(data)
    save_image(img, filename)

def advance_qr_generator(f_color, b_color):
    data = qr_data()
    filename = file_name()

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=f_color, back_color=b_color)
    save_image(img, filename)

# simple_qr_generator()
advance_qr_generator("white", "black")