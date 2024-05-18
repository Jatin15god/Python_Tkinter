from tkinter import messagebox, simpledialog
from tkinter import *
import tkinter as tk
from ttkbootstrap import *

root = Window(title="Task App", themename="solar", resizable=(False,False))
root.geometry("350x400")


tasks = []

def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task():
    task = taskEntry.get().strip()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        taskEntry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        listbox.delete(task_index)
        del tasks[task_index]
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def mark_complete():
    task_index = listbox.curselection()
    if task_index:
        index = task_index[0]
        
        listbox.itemconfig(index, {'bg': 'green'}) # Change background color to indicate completion
        messagebox.showinfo("Success", "Task marked as complete.")
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as complete.")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                task = line.strip()
                tasks.append(task)
                listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass

def edit_task():
    selected_index = listbox.curselection()
    if selected_index:
        old_task = tasks[selected_index[0]]
        new_task = simpledialog.askstring("Edit", "Edit Task", initialvalue=old_task)
        if new_task:
            tasks[selected_index[0]] = new_task
            listbox.delete(selected_index[0])  # Delete the old task from the listbox
            listbox.insert(selected_index[0], new_task)  # Insert the edited task in the same index
            save_tasks()  # Save the updated tasks to file
    else:
        messagebox.showwarning("Warning", "Please select a task to Edit.")



label = Label(root, text="Task App", font=('Helvetica', 30), underline=True)
label.grid(row=0,column=1,pady=10, padx=10, sticky='ew')

Label(root,text="Enter Task : ").grid(row=1,column=0, pady=20, padx=5)
taskEntry=Entry(font=('Arial'))
taskEntry.grid(row=1,column=1, sticky='ew')

addButton = Button(root, text="Add", command=add_task)
addButton.grid(row=1, column=2, sticky='ew', padx=10)

listbox = Listbox(root, width=30, height=10)
listbox.grid(row=2, column=0, rowspan=3, columnspan=2, sticky="nsew", padx=6)

delButton = Button(root, text="Delete", command=delete_task)
delButton.grid(row=2, column=2, sticky='ew', padx=10)

markButton = Button(root, text="Mark", command=mark_complete)
markButton.grid(row=3, column=2, sticky='ew', padx=10)

editButton = Button(root, text="Edit", command=edit_task)
editButton.grid(row=4, column=2, sticky='ew', padx=10)

load_tasks()

root.mainloop()