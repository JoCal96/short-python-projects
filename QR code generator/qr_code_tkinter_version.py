import tkinter as tk
from tkinter.filedialog import asksaveasfilename
import qrcode
from PIL import Image, ImageColor

generated_img = None

def creation():
    global generated_img
    website_link = ent_website_link.get()
    qr_color = ent_qr_color.get()
    back_color = ent_back_color.get()

    qr_color_choice = ImageColor.getcolor(qr_color, "RGB")
    back_color_choice = ImageColor.getcolor(back_color, "RGB")

    qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
    qr.add_data(website_link)
    qr.make(fit=True)

    generated_img = qr.make_image(fill_color = qr_color_choice, back_color = back_color_choice)
    print("QR Code generated - Please click save.")
    return generated_img

def save():
    global generated_img

    if generated_img is None:
        print("No QR Code generated to save.")
        return
    
    filepath = asksaveasfilename(
        defaultextension=".png",
        filetypes=[("Image Files", ".png"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    generated_img.save(filepath)
    print(f"QR Code saved as {filepath}")


window = tk.Tk()
window.title("QR Code Generator")

window.rowconfigure(0, minsize = 300, weight=1)
window.columnconfigure(1, weight=1)

frm_entry = tk.Frame(master=window)
frm_entry.grid(row=0, column=0, padx=5, pady=2, sticky='n')

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

frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text="Generate", command=creation)
btn_save = tk.Button(frm_buttons, text="Save", command=save)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

frm_buttons.grid(row=0, column=0, sticky='w')

window.mainloop()