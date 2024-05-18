from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
root.title("TTK Bootstrap! Floodgauge")
root.geometry('800x600')
#root.iconbitmap('Desktop\Python\lam.png')

def stuff(x):
    my_menu.config(bootstyle=x)
    my_label.config(text=f"You selected {x}")

my_menu = tb.Menubutton(root, bootstyle="warning", text="Things")
my_menu.pack(pady=10)

#Create Menu
inside_Menu = tb.Menu(my_menu)

#Add items inside menu
item_var = StringVar()
for x in ['primary', 'secondary', 'danger', 'info', 'outline primary', 'outline secondary']:
    inside_Menu.add_radiobutton(label=x, variable=item_var, command= lambda x=x:stuff(x)) #for tkinter, you need to create a lambda
                                                            #x=x is done to avoid overriding, otherwise it will print last item only
    
#Associate inside menu with Menubutton
my_menu['menu'] = inside_Menu

my_label = tb.Label(root, text="")
my_label.pack(pady=10)

root.mainloop()