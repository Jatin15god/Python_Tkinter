from ttkbootstrap import Window, Label, Entry, Button

root = Window(title="Contra", scaling="2", themename="solar", resizable=(False, False))

label = Label(root, text="Contra 2028", bootstyle=('Helvetica'))
# label.pack(pady=20)

label1 = Label(root, text="Name : ")
enter1 = Entry(root)
label1.grid(row=0, column=1)
enter1.grid(row=0, column=2)
label2 = Label(root, text="Id : ")
enter2 = Entry(root)
label2.grid(row=1, column=1)
enter2.grid(row=1, column=2)
label13 = Label(root, text="First Game : ")
enter13 = Entry(root)
label13.grid(row=2, column=1)
enter13.grid(row=2, column=2)

def insertData():
    root.destroy()

Button(root, text="Add Student", bootstyle="success", command=insertData).grid(columnspan=5, row=3, column=2)

root.mainloop()