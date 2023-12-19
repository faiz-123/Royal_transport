from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
from functools import partial
from database_handle import *
import re
import ast
from tkcalendar import DateEntry
from datetime import date,datetime
import calendar

import locale

def Set_Bg_Image(self,image_path):
    self.bg_image = PhotoImage(file=image_path)
    self.bg_label = Label(self.root, image=self.bg_image)
    self.bg_label.place(relx=0.5, rely=0.5, anchor="center")

def Button_Image(self,w,h,**img):
    img= img.get('img',None)
    if img:
        image_path = img
    else:
        image_path = r"traonsport_images/button.png"
    image = Image.open(image_path)
    resize_image = image.resize((w,h))
    self.img = ImageTk.PhotoImage(resize_image)

    return self.img

def to_uppercase(*args):
    args[0].set(args[0].get().upper())

def to_digit(*args):
    if not args[0].get().isdigit():
        args[1].set(args[0].get()[:len(args[0].get())-1])

def format_currency(amount):
    # Set the locale to Indian English
    locale.setlocale(locale.LC_NUMERIC, 'en_IN')

    # Format the amount with commas
    formatted_amount = locale.format_string("%.2f", amount, grouping=True)

    # Add the Rupee symbol
    formatted_amount = '₹ ' + formatted_amount

    return formatted_amount

def is_dict_string(s):
    try:
        # Attempt to evaluate the string as a literal
        ast.literal_eval(s)
        # Check if the evaluated object is a dictionary
        return isinstance(ast.literal_eval(s), dict)
    except (SyntaxError, ValueError):
        return False

def set_style():
    s = ttk.Style()
    s.theme_use('clam')
    s.configure('Treeview', rowheight=35)
    s.configure('Treeview.Heading', background="#2664AD", foreground="white",
                font=("times new roman", 11, "bold"), releif=FLAT)

    s.map('Treeview.Heading', background=[('active', '#2664AD')])
    s.configure('C', rowheight=30)

def get_data_from_database(table_name,index):
    data = fetch_data(table_name=table_name)
    if index=='all':
        data_list = data
    else:
        data_list = [dat[index] for dat in data]

    return data_list




