import tkinter as tk
import tkinter.filedialog as fd
import imageio.v3 as iio
from PIL import Image
import numpy as np

images = None

def select_files(desired_size=(256, 256)):
    global images
    filenames = fd.askopenfilenames(parent=window, title="Choose Files", multiple=True)
    selected_files = list(filenames)
    images = []
    
    for filename in selected_files:
        image = (iio.imread(filename))
        pil_image = Image.fromarray(image)
        resized = pil_image.resize(desired_size)
        resized_array = np.asarray(resized)
        images.append(resized_array)
        
    return images

def gif_save():
    global images
    filepath = fd.asksaveasfilename(
        defaultextension=".gif",
        filetypes=[("Image Files", ".gif"), ("All Files", "*.*")],
    )
    iio.imwrite(filepath, images, duration = 500, loop = 0)

window = tk.Tk()
window.title("GIF Creator")

window.rowconfigure(1, weight=1)
window.columnconfigure(1, weight=1)

main_title = tk.Label(master=window, text="GIF GENERATOR")
main_title.grid(row=0, column=0, columnspan=3,sticky='n')

form_frame = tk.Frame(master=window)
form_frame.grid(row=1, column=0, columnspan= 4, padx=5, sticky='n')

selector_lbl = tk.Label(master=form_frame, text="Step 1: Choose your images.\nRecommended size = 256x256px (images will be resized)", justify="left")
image_selector_ent = tk.Button(master=form_frame, text="File Explorer", command=select_files)
selector_lbl.grid(row=0, column=0, columnspan=3, sticky='nw')
image_selector_ent.grid(row=1, column=0, sticky='n')

save_lbl = tk.Label(master=form_frame, text="Step 2: Save your created GIF.\nYou can select your file name and save location.",justify="left")
gif_save = tk.Button(master=form_frame, text="Save", command=gif_save)
save_lbl.grid(row=2, column=0, columnspan=3, sticky='nw')
gif_save.grid(row=3, column=0, sticky='n')

window.mainloop()