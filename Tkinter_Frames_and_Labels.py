from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
root.title("TTK Bootstrap! Floodgauge")
root.geometry('800x600')
#root.iconbitmap('Desktop\Python\lam.png')

def thing():
    pass

my_frame = tb.Frame(root,  bootstyle="dark")
my_frame.pack(pady=10)

#my_frame = Frame(root)
#my_frame.pack(pady=10) #For Simple Frame with no background

my_entry = tb.Entry(my_frame, font=("Helvetica", 18))
my_entry.pack(pady=10, padx=20)

my_button = tb.Button(my_frame, text="Click", bootstyle=DANGER+OUTLINE, command=thing)
my_button.pack(padx=20, pady=10)

my_label = tb.Label(root,text="Hello There!", font=("Helvetica", 18), bootstyle="inverse light")
my_label.pack(pady=10, padx=20)



root.mainloop()