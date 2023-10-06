# Function for displaying the to-do list
def display_tasks():
    with open("todolist.txt", "r") as file:
        tasks = file.readlines()
        if not tasks:
            print("Your to-do list is empty.")
        else:
            print("Your to-do list:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")

# Function to adding task
def add_task(task):
    with open("todolist.txt", "a") as file:
        file.write(task + "\n")
    print(f"Task '{task}' added to your to-do list.")

# Function to removing a task 
def remove_task(task_number):
    with open("todolist.txt", "r") as file:
        tasks = file.readlines()
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        with open("todolist.txt", "w") as file:
            file.writelines(tasks)
        print(f"Task '{removed_task.strip()}' removed from your to-do list.")
    else:
        print("Invalid task number.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Display to-do list")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_tasks()
    elif choice == "2":
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == "3":
        display_tasks()
        task_number = int(input("Enter the task number to remove: "))
        remove_task(task_number)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")

