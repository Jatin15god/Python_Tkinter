from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
root.title("TTK Bootstrap")
root.geometry('800x600')
#root.iconbitmap('Desktop\Python\lam.png')

counter = 0
def changer1():
    global counter
    counter+=1
    if counter %2 == 0:
        my_label.config(text="Hello World")
    else:
        my_label.config(text="GoodBye World")

def changer2():
    global counter
    counter+=1
    if counter %2 == 0:
        my_label3.config(text="Hello World!")
    else:
        my_label3.config(text="Bye World!")

my_label = tb.Label(text="Hello World", font=("Helvetica", 18), bootstyle="info, inverse")
my_label.pack(pady=50)
my_label2 = tb.Button(text="Click me", bootstyle="success, outline", command=changer1)
my_label2.pack(pady=10)
my_label3 = tb.Button(text="Click me", bootstyle="default, link", command=changer2)
my_label3.pack(pady=10)

Check_label = tb.Checkbutton(text="Check", bootstyle="default", command=changer2)
Check_label.pack(pady=10)

#Size of button

my_style = tb.Style()
my_style.configure('success.Outline.TButton', font=("Helvetica", 28))
my_label4 = tb.Button(text="Hello World",bootstyle="danger", width=30, style="success.Outline.TButton")
my_label4.pack(pady=40)

root.mainloop()