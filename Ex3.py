import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        
        self.style = Style(theme="flatly")
        
        self.tasks = []
        
        self.create_widgets()
        
    def create_widgets(self):
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(pady=10)
        
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack()
        
        self.task_listbox = tk.Listbox(self.root, height=15)
        self.task_listbox.pack(pady=10)
        
        self.complete_button = tk.Button(self.root, text="Mark Complete", command=self.mark_complete)
        self.complete_button.pack(side=tk.LEFT, padx=10)
        
        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.RIGHT, padx=10)
        
        self.load_tasks()
        
    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
            
    def mark_complete(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.task_listbox.itemconfig(task_index, {'bg': '#d9ead3'})  # Change background color to indicate completion
            messagebox.showinfo("Success", "Task marked as complete.")
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as complete.")
            
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.task_listbox.delete(task_index)
            del self.tasks[task_index]
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")
            
    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(task + "\n")
                
    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                for line in f:
                    task = line.strip()
                    self.tasks.append(task)
                    self.task_listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
