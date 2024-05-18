from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
root.title("TTK Bootstrap")
root.geometry('800x600')
#root.iconbitmap('Desktop\Python\lam.png')

def checker():
    if var1.get() == 1:
        my_label.config(text="Checked")
    else:
        my_label.config(text="UnChecked")

Check_label = tb.Checkbutton(text="Check", bootstyle="default")
Check_label.pack(pady=10)

my_label = tb.Label(text="Check the box", font=("Helvetica", 18), bootstyle="info, inverse")
my_label.pack(pady=(40,10))

var1 = IntVar()
my_check = tb.Checkbutton(text="Check the box", bootstyle="info", variable = var1, onvalue = 1, offvalue = 0, command = checker)
my_check.pack(pady=10)

var2 = IntVar()
my_check2 = tb.Checkbutton(text="Check the box", bootstyle="danger, toolbutton", variable = var2, onvalue = 1, offvalue = 0, command = checker)
my_check2.pack(pady=10)

var3 = IntVar()
my_check3 = tb.Checkbutton(text="Check the box", bootstyle="outlined toolbutton", variable = var3, onvalue = 1, offvalue = 0, command = checker)
my_check3.pack(pady=10)

var4 = IntVar()
my_check4 = tb.Checkbutton(text="Check the box", bootstyle="success, round-toggle", variable = var1, onvalue = 1, offvalue = 0, command = checker)
my_check4.pack(pady=10)

var5 = IntVar()
my_check5 = tb.Checkbutton(text="Check the box", bootstyle="warning, square-toggle", variable = var5, onvalue = 1, offvalue = 0, command = checker)
my_check5.pack(pady=10)

#Size of button

my_style = tb.Style()
my_style.configure('success.TCheckbutton', font=("Helvetica", 28))
my_label4 = tb.Checkbutton(text="Hello World",bootstyle="danger", width=30, style="success.TCheckbutton")
my_label4.pack(pady=40)

root.mainloop()