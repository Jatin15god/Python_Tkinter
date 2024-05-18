from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
root.title("TTK Bootstrap! Entry Box")
root.geometry('800x600')
#root.iconbitmap('Desktop\Python\lam.png')

def speak():
    my_label.config(text=f'You Typed: {my_entry.get()}')

my_entry = tb.Entry(root, bootstyle="success", font=("Helvetica", 18), foreground="red", width=15, show="$")
my_entry.pack(pady=50)

my_button = tb.Button(root, bootstyle="success outline", text="Click Me", command=speak)
my_button.pack(pady=20)

my_label = tb.Label(root, text="")
my_label.pack(pady=20)

root.mainloop()