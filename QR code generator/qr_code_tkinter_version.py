import re
import tkinter as tk
from tkinter.filedialog import asksaveasfilename
import qrcode
from PIL import Image, ImageColor

def url_check(url):
    regex = re.compile(
            r'^(?:http|ftp)s?://'
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'
            r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'
            r'(?::\d+)?'
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None        

generated_img = None

def creation():
    global generated_img
    website_link = ent_website_link.get()
    qr_color = ent_qr_color.get()
    back_color = ent_back_color.get()

    try: 
        if not url_check(website_link):
            lbl_create.config(text="Invalid website link")
            raise ValueError("Invalid website link")
        
        qr_color_choice = ImageColor.getcolor(qr_color, "RGB")
        back_color_choice = ImageColor.getcolor(back_color, "RGB")

        qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
        qr.add_data(website_link)
        qr.make(fit=True)

        generated_img = qr.make_image(fill_color = qr_color_choice, back_color = back_color_choice)
        lbl_create.config(text="QR Code generated. Please click save")
    except ValueError as e:
        lbl_create.config(text=f"Error: {e}")
        generated_img = None
        
    return generated_img

def save():
    global generated_img

    if generated_img is None:
        lbl_create.config(text="No QR Code generated to save.")
        return
    
    filepath = asksaveasfilename(
        defaultextension=".png",
        filetypes=[("Image Files", ".png"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    generated_img.save(filepath)
    lbl_create.config(text="QR Code saved")


window = tk.Tk()
window.title("QR Code Generator")

window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

lbl_title = tk.Label(master=window, text="QR CODE GENERATOR")
lbl_title.grid(row=0, column=0, columnspan=3, pady=3)

frm_entry = tk.Frame(master=window)
frm_entry.grid(row=1, column=0, padx=5, pady=5, sticky='n')

ent_website_link = tk.Entry(master=frm_entry, width=70)
lbl_website_link = tk.Label(master=frm_entry, text="Input the website link to become a QR Code: ")
ent_website_link.grid(row=0,column=1,sticky='e')
lbl_website_link.grid(row=0,column=0,sticky='w')

ent_qr_color = tk.Entry(master=frm_entry, width=70)
lbl_qr_color = tk.Label(master=frm_entry, text="Choose a QR color (e.g., 'black', 'green'): ")
ent_qr_color.grid(row=1,column=1,sticky='e')
lbl_qr_color.grid(row=1,column=0,sticky='w')

ent_back_color = tk.Entry(master=frm_entry, width=70)
lbl_back_color = tk.Label(master=frm_entry, text="Choose a background color (e.g., 'white', 'red'): ")
ent_back_color.grid(row=2,column=1,sticky='e')
lbl_back_color.grid(row=2,column=0,sticky='w')

lbl_create = tk.Label(master=frm_entry, text="Click generate to create your custom QR code.")
lbl_create.grid(row=3, column=0, pady=10, columnspan=2)

frm_buttons = tk.Frame(master=window, relief=tk.RAISED, bd=2)
frm_buttons.grid(row=2, column=0, pady=5, padx=5, sticky='n')

btn_create = tk.Button(master=frm_buttons, text="Generate", command=creation)
btn_save = tk.Button(master=frm_buttons, text="Save", command=save)
btn_create.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
btn_save.grid(row=0, column=2, sticky="ew", padx=5, pady=5)


window.mainloop()