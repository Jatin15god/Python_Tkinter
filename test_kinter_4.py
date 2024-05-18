from PIL import Image
Image.CUBIC = Image.BICUBIC
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# All I did to resolve issue of PIL image is performing line 1 and 2
# For more explaination : https://stackoverflow.com/questions/76717279/ttkbootstrap-meter-widget-doc-example-not-working

app = ttk.Window()

meter = ttk.Meter(
    metersize=180,
    padding=5,
    amountused=25,
    metertype="semi",
    subtext="miles per hour",
    interactive=True,
)
meter.pack()

# update the amount used directly
meter.configure(amountused = 50)

# update the amount used with another widget
entry = ttk.Entry(textvariable=meter.amountusedvar)
entry.pack(fill=X)

# increment the amount by 10 steps
meter.step(10)

# decrement the amount by 15 steps
meter.step(-15)

# update the subtext
meter.configure(subtext="loading...")

app.mainloop()