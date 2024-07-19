import qrcode
from PIL import Image, ImageColor

def creation():
    website_link = input(str("Input the website link to become a QR Code: "))
    qr_color = input("Choose a QR color (e.g., 'black', 'green'): ")
    back_color = input("Choose a background color (e.g., 'white', 'red'): ")
    file_name = input("Input a QR code file name (if empty file name will be QR_Code): ")

    mode = "RGB"
    qr_color_choice = ImageColor.getcolor(qr_color, mode)
    back_color_choice = ImageColor.getcolor(back_color, mode)

    qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
    qr.add_data(website_link)
    qr.make()

    img = qr.make_image(fill_color = qr_color_choice, back_color = back_color_choice)
    print("QR Code generated - Please click save.")
    return file_name, img

def save(file_name, img):
    if file_name == "" :
        img.save('QR_Code.png')
    else:
        img.save(f'{file_name}.png')