from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
root.title("TTK Bootstrap! Floodgauge")
root.geometry('800x600')
#root.iconbitmap('Desktop\Python\lam.png')

def starter():
    my_gauge1.start()
    my_gauge2.start()

def stopper():
    my_gauge1.stop()
    my_gauge2.stop()

def incrementer():
    my_gauge1.step(5)
    my_gauge2.step(5)
    my_label.config(text=f"Position: {my_gauge1.variable.get()+10}")

def resetter():
    my_gauge1.configure(value=10)
    my_gauge2.configure(value=10)


#First
my_gauge1 = tb.Floodgauge(root, bootstyle=SUCCESS, font=("Helvetica", 18), mask="Per: {}%", maximum=100, orient=HORIZONTAL, value=10) # Default is Determinate
my_gauge1.pack(pady=20, fill=X, padx=10)

#Second
my_gauge2 = tb.Floodgauge(root, bootstyle=SUCCESS, font=("Helvetica", 18), mask="Per: {}%", maximum=80, orient=HORIZONTAL, value=10, mode=INDETERMINATE)
my_gauge2.pack(pady=20, fill=X, padx=10)

start_button = tb.Button(root, text="Start", bootstyle=DANGER+OUTLINE, command=starter)
start_button.pack(padx=20, fill=X)

stop_button = tb.Button(root, text="Stop", bootstyle=DANGER+OUTLINE, command=stopper)
stop_button.pack(padx=20, fill=X)

Inc_button = tb.Button(root, text="Increase", bootstyle=DANGER+OUTLINE, command=incrementer)
Inc_button.pack(padx=20, fill=X)

reset_button = tb.Button(root, text="Reset", bootstyle=DANGER+OUTLINE, command=resetter)
reset_button.pack(padx=20, fill=X)

my_label = tb.Label(root, text="Position:     ")
my_label.pack(pady=10)


def Nstarter():
    my_gauge3.start()


#New
my_gauge3 = tb.Floodgauge(root, bootstyle=SUCCESS, font=("Helvetica", 18), mask="Per: {}%", maximum=101, orient=VERTICAL, value=10)
my_gauge3.pack(pady=20)

start_button1 = tb.Button(root, text="Start", bootstyle=DANGER+OUTLINE, command=Nstarter)
start_button1.pack(padx=20, fill=X)

def my_upd(*args):
    if my_gauge3.variable.get() < 25:
        my_gauge3.configure(bootstyle=INFO)
    elif my_gauge3.variable.get() < 50:
        my_gauge3.configure(bootstyle=SUCCESS)
    elif my_gauge3.variable.get() < 80:
        my_gauge3.configure(bootstyle=WARNING)
    elif my_gauge3.variable.get() == 100:
         my_gauge3.stop()
    else:
        my_gauge3.configure(bootstyle=DANGER)

my_gauge3.variable.trace("w", my_upd)

root.mainloop()