from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
root.title("TTK Bootstrap! Combobox")
root.geometry('800x600')
#root.iconbitmap('Desktop\Python\lam.png')

def clicker():
    my_label.config(text=f"You Selected {my_combo.get()}!")

def click_bind(e):
     my_label.config(text=f"You Selected {my_combo.get()}!")

my_label = tb.Label(root, text="Combobox", font=("Helvetica", 18), bootstyle="info, inverse")
my_label.pack(pady=40)

#Create days List
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#Combobox
my_combo = tb.Combobox(root, bootstyle="success", values=days)
my_combo.pack(pady=40)

#default day
my_combo.current(0)

my_button = tb.Button(root, text="Click Me!", command=clicker, bootstyle="success")
my_button.pack(pady=40)

#Bind the Combobox
my_combo.bind("<<ComboboxSelected>>", click_bind)

root.mainloop()