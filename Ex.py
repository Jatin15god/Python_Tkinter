import tkinter as tk
from tkinter import ttk
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

        self.view_button = ttk.Button(master, text="View All Tasks", command=self.view_all_tasks)
        self.view_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def mark_as_complete(self):
        selection = self.task_list.curselection()
        if selection:
            index = selection[0]
            self.task_list.itemconfig(index, {'foreground': 'gray'})
            self.task_list.selection_clear(index)
    
    def delete_task(self):
        selection = self.task_list.curselection()
        if selection:
            index = selection[0]
            del self.tasks[index]
            self.task_list.delete(index)

    def view_all_tasks(self):
        if self.tasks:
            all_tasks = '\n'.join(self.tasks)
            tk.messagebox.showinfo("All Tasks", all_tasks)
        else:
            tk.messagebox.showinfo("All Tasks", "No tasks available.")

def main():
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()
