import tkinter as tk

def convert():
    numeral = ent_roman_numeral.get()

    converted_int = 0

    if "CM" in numeral:
        converted_int += 900
        numeral = numeral.replace("CM", "")
    if "CD" in numeral:
        converted_int += 400
        numeral = numeral.replace("CD", "")
    if "XC" in numeral:
        converted_int += 90
        numeral = numeral.replace("XC", "")
    if "XL" in numeral:
        converted_int += 40
        numeral = numeral.replace("XL", "")
    if "IX" in numeral:
        converted_int += 9
        numeral = numeral.replace("IX", "")
    if "IV" in numeral:
        converted_int += 4
        numeral = numeral.replace("IV", "")

    for i in numeral:
        if i == "M":
            converted_int += 1000
        elif i == "D":
            converted_int += 500
        elif i == "C":
            converted_int += 100
        elif i == "L":
            converted_int += 50
        elif i == "X":
            converted_int += 10
        elif i == "V":
            converted_int += 5
        elif i == "I":
            converted_int += 1

    return converted_int, lbl_return_message.config(text="The roman numerals you entered translates to: " + str(converted_int) + "!")


window = tk.Tk()
window.title("Roman Numeral Converter")

window.rowconfigure(1, weight=1)
window.columnconfigure(1, weight=1)

lbl_page_title = tk.Label(master=window, text="Roman Numeral Converter")
lbl_page_title.pack(expand='yes', fill='both')

frm_entry = tk.Frame(master=window)
frm_entry.pack(fill='x', anchor='w', pady=5, padx=5)

lbl_roman_numeral = tk.Label(master=frm_entry, text="Enter Roman Numeral: ", justify="left")
ent_roman_numeral = tk.Entry(master=frm_entry, width=20)
lbl_roman_numeral.pack(side="left")
ent_roman_numeral.pack(side="left")

frm_convert = tk.Frame(master=window)
frm_convert.pack(fill='x', anchor='w', pady=5, padx=5)

lbl_convert_message = tk.Label(master=frm_convert, text="Click convert: ", justify="left")
lbl_convert_message.pack(side="left")

btn_convert = tk.Button(master=frm_convert, text="Convert", relief="raised", command=convert)
btn_convert.pack(side="left")

frm_return = tk.Frame(master=window)
frm_return.pack(fill="both", expand=True, pady=5, padx=5)

lbl_return_message = tk.Label(master=frm_return, text="The roman numerals you entered translates to: ", justify="center")
lbl_return_message.pack(fill='x', anchor='w')

window.mainloop()

