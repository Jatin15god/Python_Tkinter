from time import sleep

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
            sleep(2)

    def delete_task(self, task_number):
        try:
            self.tasks.pop(task_number - 1)
        except IndexError:
            print("Invalid Input")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List\n")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Quit")

        choice = int(input("Enter Choice : "))

        if choice > 4 or choice < 1:
            print("Invalid Input.")
        else:
            match choice:
                case 1: todo_list.add_task(input("Enter Task : "))
                case 2: todo_list.view_tasks()
                case 3: todo_list.delete_task(int(input("Enter Task Number : ")))
                case 4: break
        
        print("End.")

if __name__ == "__main__":
    main()
