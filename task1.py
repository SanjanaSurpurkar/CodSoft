class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def complete_task(self, index):
        del self.tasks[index]

    def save_to_file(self, file):
        with open(file, 'w') as f:
            for task in self.tasks:
                f.write(task + '\n')

    def load_from_file(self, file):
        with open(file, 'r') as f:
            self.tasks = [line.strip() for line in f]


def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Save Tasks to File")
        print("5. Load Tasks from File")
        print("6. Quit")

        ch = input("Enter your choice: ")

        if ch == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif ch == '2':
            todo_list.view_tasks()
        elif ch == '3':
            index = int(input("Enter task number to complete: ")) - 1
            todo_list.complete_task(index)
        elif ch == '4':
            file = input("Enter filename to save tasks to: ")
            todo_list.save_to_file(file)
        elif ch == '5':
            file = input("Enter filename to load tasks from: ")
            todo_list.load_from_file(file)
        elif ch == '6':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
