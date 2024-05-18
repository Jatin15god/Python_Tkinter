import tkinter as tk
from tkinter import messagebox

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
        listbox.itemconfig(index, {'bg': '#d9ead3'})  # Change background color to indicate completion
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
    pass