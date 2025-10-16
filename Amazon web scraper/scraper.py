import requests
from bs4 import BeautifulSoup
import tkinter as tk

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
  'Accept-Language': 'en-US,en;q=0.5'}

def get_product_details() -> dict:
    product_url = ent_product_url.get()
    details = {}
    try:
        page = requests.get(product_url, headers=headers)
        soup = BeautifulSoup(page.content, features='lxml')
        
        title = soup.find('span', attrs={'id':'productTitle'}).get_text().strip()

        extracted_price = soup.find('span', attrs={'class':'a-price'}).get_text().strip()
        price = '£' + extracted_price.split('£') [1]

        availability = soup.find('div', attrs={'id':'availability'}).get_text().strip()
        
        details['Title'] = title
        details['Price'] = price
        details['Availability'] = availability
        
        formatted_details = "\n".join(f"{key}: {value}" for key, value in details.items())
        
        return details, frm_returned_info.config(text=formatted_details)
    except Exception as e:
        print(f'Failed to retrieve procduct details with error: {e}')

# product_url = input('Enter product url: ')
# product_details = get_product_details(product_url)
# print(product_details)


window = tk.Tk()
window.title("Amazon Product Info Finder")
window.rowconfigure(1, weight=1)
window.columnconfigure(1, weight=1)

lbl_page_title = tk.Label(master=window, text="Amazon Product Info Finder")
lbl_page_title.pack(expand='yes', fill='both')

frm_entry = tk.Frame(master=window)
frm_entry.pack(fill='x', anchor='w', pady=5, padx=5)

lbl_product_url = tk.Label(master=frm_entry, text='Enter product url: ', justify="left")
ent_product_url = tk.Entry(master=frm_entry, width=85)
lbl_product_url.pack(side="left")
ent_product_url.pack(side="left")

frm_enter = tk.Frame(master=window)
frm_enter.pack(fill='x', anchor='w', pady=5, padx=5)
btn_enter_button = tk.Button(master=frm_enter, text="Get Product Info", relief="raised", command=get_product_details)
btn_enter_button.pack(side="left")

frm_returned = tk.Frame(master=window)
frm_returned.pack(fill="both", expand=True, pady=5, padx=5)
frm_returned_info = tk.Label(master=frm_returned, justify="left", anchor="w")
frm_returned_info.pack(fill='x', anchor='w')

window.mainloop()