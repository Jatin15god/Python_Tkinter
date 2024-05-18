from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttk

root = ttk.Window(themename="superhero")
root.title("TTK Bootstrap! Floodgauge")
root.geometry('800x600')

mb = ttk.Menubutton(root, text='My widgets', style='info.Outline.TMenubutton')
mb.pack(pady=20)

# create menu
menu = ttk.Menu(mb)

# add options
option_var = ttk.StringVar()
for option in ['option 1', 'option 2', 'option 3']:
    menu.add_radiobutton(label=option, value=option, variable=option_var)

# associate menu with menubutton
mb['menu'] = menu

root.mainloop()