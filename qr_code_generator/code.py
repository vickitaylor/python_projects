# install all librarys needed (qrcode and image)
# create a function that collects a text and converts to a qr code
# save qr code as an image

import qrcode

def generate_qrcode(text):
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="purple", back_color="white")
    img.save("qrimg001.png")


url = input("Enter your URL or phrase:")
generate_qrcode(url)
