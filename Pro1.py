import tkinter as tk
from tkinter import messagebox
import mysql.connector

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

class TaskManagerApp:
    def __init__(self, master):
        self.master = master
        master.title("Task Manager")

        self.tasks = []

        self.title_label = tk.Label(master, text="Task Title:")
        self.title_label.pack()

        self.title_entry = tk.Entry(master)
        self.title_entry.pack()

        self.desc_label = tk.Label(master, text="Task Description:")
        self.desc_label.pack()

        self.desc_entry = tk.Entry(master)
        self.desc_entry.pack()

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.edit_button = tk.Button(master, text="Edit Task", command=self.edit_task)
        self.edit_button.pack()

        self.complete_button = tk.Button(master, text="Complete Task", command=self.complete_task)
        self.complete_button.pack()

        self.list_button = tk.Button(master, text="List Tasks", command=self.list_tasks)
        self.list_button.pack()

        self.task_listbox = tk.Listbox(master)
        self.task_listbox.pack()

        self.new_task_description_entry = tk.Entry(master)
        self.new_task_description_entry.pack()

        self.new_task_assignee_entry = tk.Entry(master)
        self.new_task_assignee_entry.pack()

        self.new_task_status_combo = tk.StringVar()
        self.new_task_status_combo.set("Not Started")
        self.new_task_status = tk.OptionMenu(master, self.new_task_status_combo, "Not Started", "In Progress", "Completed")
        self.new_task_status.pack()

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

    def edit_task(self):
        selected_task_id = self.task_listbox.curselection()
        if len(selected_task_id) == 0:
            messagebox.showerror("Error", "No task selected")
            return
        selected_task_id = selected_task_id[0]
        selected_task = self.task_listbox.get(selected_task_id)
        task_data = selected_task.split(" - ")
        task_id = task_data[0].strip("[]")
        old_description = task_data[1].strip()
        old_assignee = task_data[2].strip()
        old_status = task_data[3].strip()

        new_description = self.new_task_description_entry.get()
        new_assignee = self.new_task_assignee_entry.get()
        new_status = self.new_task_status_combo.get()

        self.update_task(task_id, new_description, new_assignee, new_status)

        # Refresh the task listbox
        self.load_tasks()

        # Clear the input fields
        self.new_task_description_entry.delete(0, tk.END)
        self.new_task_assignee_entry.delete(0, tk.END)
        self.new_task_status_combo.set("Not Started")

    def complete_task(self):
        selected_task_id = self.task_listbox.curselection()
        if len(selected_task_id) == 0:
            messagebox.showerror("Error", "No task selected")
            return
        selected_task_id = selected_task_id[0]
        selected_task = self.task_listbox.get(selected_task_id)
        task_data = selected_task.split(" - ")
        task_id = task_data[0].strip("[]")

        self.complete_task_db(task_id)

        # Refresh the task listbox
        self.load_tasks()

    def list_tasks(self):
        if self.tasks:
            task_list = "\n".join([f"{task.title}: {task.description} {'(Completed)' if task.completed else ''}" for task in self.tasks])
            messagebox.showinfo("Task List", task_list)
        else:
            messagebox.showinfo("Task List", "No tasks to display.")

    def update_task(self, task_id, new_description, new_assignee, new_status):
        # Connect to the MySQL database
        mydb = mysql.connector.connect(
          host="localhost",
          user="your_username",
          password="your_password",
          database="task_management"
        )

        # Create a cursor object
        mycursor = mydb.cursor()

        # Update the task in the tasks table
        sql = "UPDATE tasks SET description=%s, assignee=%s, status=%s WHERE id=%s"
        val = (new_description, new_assignee, new_status, task_id)
        mycursor.execute(sql, val)

        #Commit the changes and close the connection
        mydb.commit()
        mydb.close()

    def complete_task_db(self, task_id):
        # Connect to the MySQL database
        mydb = mysql.connector.connect(
          host="localhost",
          user="your_username",
          password="your_password",
          database="task_management"
        )

        # Create a cursor object
        mycursor = mydb.cursor()

        # Update the task in the tasks table
        sql = "UPDATE tasks SET completed=1 WHERE id=%s"
        val = (task_id, )
        mycursor.execute(sql, val)

        # Commit the changes and close the connection
        mydb.commit()
        mydb.close()

    def load_tasks(self):
        # Connect to the MySQL database
        mydb = mysql.connector.connect(
          host="localhost",
          user="your_username",
          password="your_password",
          database="task_management"
        )

        # Create a cursor object
        mycursor = mydb.cursor()

        # Get all tasks from the tasks table
        mycursor.execute("SELECT * FROM tasks")

        # Clear the current task list
        self.task_listbox.delete(0, tk.END)

        # Add each task to the task list
        for row in mycursor.fetchall():
            task_id, title, description, assignee, status, completed = row
            task_status = "Completed" if completed else "Not Started"
            task_string = f"[{task_id}] {title}: {description} ({task_status})"
            self.task_listbox.insert(tk.END, task_string)

        mydb.close()

def main():
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()