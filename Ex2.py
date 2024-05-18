import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style

class TaskManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Task Manager")
        
        self.style = Style(theme='minty')
        self.style.configure('.', font=('Helvetica', 12))

        self.tasks = []

        self.task_entry = ttk.Entry(master, width=40)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        self.add_button = ttk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.task_list = tk.Listbox(master, width=50)
        self.task_list.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.complete_button = ttk.Button(master, text="Mark as Complete", command=self.mark_as_complete)
        self.complete_button.grid(row=2, column=0, padx=5, pady=5)

        self.delete_button = ttk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=5, pady=5)

        self.save_button = ttk.Button(master, text="Save Tasks", command=self.save_tasks)
        self.save_button.grid(row=3, column=0, padx=5, pady=5)

        self.load_button = ttk.Button(master, text="Load Tasks", command=self.load_tasks)
        self.load_button.grid(row=3, column=1, padx=5, pady=5)

        self.sort_button = ttk.Button(master, text="Sort Tasks", command=self.sort_tasks)
        self.sort_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)

    def mark_as_complete(self):
        selection = self.task_list.curselection()
        if selection:
            index = selection[0]
            self.task_list.itemconfig(index, {'foreground': 'gray'})

    def delete_task(self):
        selection = self.task_list.curselection()
        if selection:
            index = selection[0]
            del self.tasks[index]
            self.update_task_list()

    def save_tasks(self):
        try:
            with open("tasks.txt", "w") as file:
                for task in self.tasks:
                    file.write(task + "\n")
            messagebox.showinfo("Success", "Tasks saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save tasks: {str(e)}")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
            self.update_task_list()
            messagebox.showinfo("Success", "Tasks loaded successfully.")
        except FileNotFoundError:
            messagebox.showerror("Error", "No saved tasks found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load tasks: {str(e)}")

    def sort_tasks(self):
        self.tasks.sort()
        self.update_task_list()

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, task)

def main():
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()
