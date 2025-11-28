import os
import time

def load_tasks():
    tasks = []
    if os.path.exists("tasks.txt"):
        with open("tasks.txt","r",encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    tasks.append(line)
    return tasks



def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet!")
    else:
        print("\nYour current tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}) {task}")

def add_tasks(tasks):
    user_input = input ("Enter your tasks separated by ';':")
    new_tasks = user_input.split(";")
    tasks.extend(new_tasks)

    view_tasks(tasks)

def delete_task(tasks):
    if not tasks:
        print("no tasks to delete.")
        return
    
    print("\nCurrent tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}) {task}")

    try:
        num = int (input("Enter the number of the task to delete: "))
        if  1<= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Task '{removed}' has been deleted.")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid")

def clear_tasks(tasks):
    tasks.clear()
    print("All tasks have been cleared!")

def save_tasks(tasks):
    with open("tasks.txt", "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

def show_menu():
    print("\n🎀 Taskly 🎀\n")
    print(f"\033[31m1.\033[0m Add new task")
    print(f"\033[31m2.\033[0m View all tasks")
    print(f"\033[31m3.\033[0m Delete task")
    print(f"\033[31m4.\033[0m Clear all tasks")
    print(f"\033[31m5.\033[0m Exit")
    print()



tasks = load_tasks()
show_menu_flag = True

while True :
    if show_menu_flag :
        show_menu()
    
    choice = input("Choose an option: ")

    match choice:
        case "1":
            add_tasks(tasks)
            save_tasks(tasks)
        case "2":
            view_tasks(tasks)
        case "3":
            delete_task(tasks)
            save_tasks(tasks)
        case "4":
            clear_tasks(tasks)
            save_tasks(tasks)
        case "5":
            print("Goodbye!")
            time.sleep(2)
            exit()
        case _:
            print("Invalid option!")
    
    again = input("Do you want to see the menu again? (yes/no): ").lower()
    if again == "yes":
        show_menu_flag = True
    else:
        show_menu_flag = False