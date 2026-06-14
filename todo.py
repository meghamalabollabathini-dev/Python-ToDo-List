tasks = []

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Search Task")
    print("5. Count Tasks")
    print("6. Edit Task")
    print("7. Clear All Tasks")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            print("\nTasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

            delete_num = int(input("Enter task number to delete: "))

            if 1 <= delete_num <= len(tasks):
                removed_task = tasks.pop(delete_num - 1)
                print(f"Task '{removed_task}' deleted successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        search = input("Enter task name to search: ")

        found = False

        for task in tasks:
            if search.lower() in task.lower():
                print("Task found:", task)
                found = True

        if not found:
            print("Task not found.")

    elif choice == "5":
        print("Total tasks:", len(tasks))

    elif choice == "6":
        if len(tasks) == 0:
            print("No tasks available to edit.")
        else:
            print("\nTasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

            edit_num = int(input("Enter task number to edit: "))

            if 1 <= edit_num <= len(tasks):
                new_task = input("Enter new task name: ")
                tasks[edit_num - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")

    elif choice == "7":
        confirm = input("Are you sure? (yes/no): ")

        if confirm.lower() == "yes":
            tasks.clear()
            print("All tasks cleared successfully!")
        else:
            print("Operation cancelled.")

    elif choice == "8":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")