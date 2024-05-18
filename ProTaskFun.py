from tkinter import messagebox
import ttkbootstrap as tk


class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

class ToDoList:
    tasks = []
    def add_task(self):
        title = self.title_entry.get()
        description = self.desc_entry.get()

        if title and description:
            new_task = Task(title, description)
            self.tasks.append(new_task)
            messagebox.showinfo("Success", "Task added successfully.")
            self.title_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill in both title and description.")