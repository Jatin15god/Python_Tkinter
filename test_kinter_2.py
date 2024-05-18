import ttkbootstrap as ttk
from ttkbootstrap.constants import *

my_w = ttk.Window()
my_w.geometry("520x320")  # width and height

fg = ttk.Floodgauge(
    bootstyle=INFO,
    mask="Progress {}%",
    value=10,
    length=500,
)
fg.grid(row=1, column=1, padx=10, pady=50, columnspan=4)

b1 = ttk.Button(my_w, text="Start", command=lambda: fg.start(), bootstyle=SUCCESS)
b1.grid(row=2, column=1, padx=10, pady=40)

b2 = ttk.Button(my_w, text="Stop", command=lambda: fg.stop(), bootstyle=DANGER)
b2.grid(row=2, column=2, padx=10, pady=40)

b3 = ttk.Button(my_w, text="Jump", command=lambda: fg.step(5), bootstyle=PRIMARY)
b3.grid(row=2, column=3, padx=10, pady=40)

b4 = ttk.Button(my_w, text="Reset", command=lambda: fg.configure(value=10), bootstyle=WARNING)
b4.grid(row=2, column=4, padx=10, pady=40)


def my_upd(*args):
    if fg.variable.get() < 25:
        fg.configure(bootstyle=INFO)
    elif fg.variable.get() < 50:
        fg.configure(bootstyle=SUCCESS)
    elif fg.variable.get() < 80:
        fg.configure(bootstyle=WARNING)
    else:
        fg.configure(bootstyle=DANGER)


fg.variable.trace("w", my_upd)
my_w.mainloop()