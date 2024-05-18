from PIL import Image
Image.CUBIC = Image.BICUBIC
from tkinter import *
#from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
root.title("TTK Bootstrap! Meter")
root.geometry('800x600')
#root.iconbitmap('Desktop\Python\lam.png')

my_meter3 = tb.Meter(root, 
                    bootstyle="danger", 
                    subtext="Tkinter Meter", 
                    interactive=True, textleft="|", 
                    textright="%", 
                    textfont="Helvetica", 
                    metertype="semi",
                    metersize=300,
                    meterthickness=50,
                    amountused=20,
                    stripethickness=10 #This Divide meter strip into divisions
                    ) 
my_meter3.pack(pady=50, side=LEFT,padx=10)

my_meter1 = tb.Meter(root, 
                    bootstyle="danger", 
                    subtext="Tkinter Meter", 
                    interactive=True, textleft="|", 
                    textright="%", 
                    textfont="Helvetica",
                    padding=10, # Just Add padding as pack
                    amounttotal=150,
                    stripethickness=10 #This Divide meter strip into divisions
                    ) 
my_meter1.pack(pady=20)

my_meter2 = tb.Meter(root, 
                    bootstyle="danger", 
                    subtext="Tkinter Meter", 
                    interactive=True, textleft="|", 
                    textright="%", 
                    textfont="Helvetica",
                    padding=10, # Just Add padding as pack
                    amounttotal=150,
                    stripethickness=10 #This Divide meter strip into divisions
                    ) 
my_meter2.pack(pady=20)

root.mainloop()