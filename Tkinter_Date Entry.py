from tkinter import *
from ttkbootstrap.dialogs import Querybox
import ttkbootstrap as tb
from datetime import date

root = tb.Window(themename="superhero")
root.title("TTK Bootstrap! Floodgauge")
root.geometry('800x600')
#root.iconbitmap('Desktop\Python\lam.png')

def dater():
    my_label.config(text=f"You Picked: {my_date.entry.get()}")

def CAL():
    cal = Querybox()
    my_label.config(text=f"You Picked: {cal.get_date()}")


my_date = tb.DateEntry(root, bootstyle="primary", firstweekday=0, startdate=date(2024, 2, 28)) # For startdate, import date from datetime
my_date.pack(pady=20)

my_button = tb.Button(root, text="Get Date", bootstyle="danger outline", command=dater)
my_button.pack(pady=20)

my_button2 = tb.Button(root, text="Get Calender", bootstyle="success link", command=CAL)
my_button2.pack(pady=20)

my_label = tb.Label(root, text="You Picked: __/__/____")
my_label.pack(pady=20)

root.mainloop()