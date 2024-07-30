def main():
    print("Welcome to the Todo List App!")
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter a new task: ")
            add_task(task)
        elif choice == '2':
            task_id = int(input("Enter the task ID to remove: "))
            remove_task(task_id)
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

def remove_task(task_id):
    if 0 <= task_id < len(tasks):
        removed_task = tasks.pop(task_id)
        print(f"Task removed: {removed_task}")
    else:
        print("Invalid task ID")

def view_tasks():
    if tasks:
        print("\nTasks:")
        for i, task in enumerate(tasks):
            print(f"{i}. {task}")
    else:
        print("No tasks available")

if __name__ == "__main__":
    main()

