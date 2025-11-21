import os

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

tasks = load_tasks()

def show_menu():
    print("\n🎀 To Do List 🎀\n")
    print(f"\033[31m1.\033[0m Add new task")
    print(f"\033[31m2.\033[0m View all tasks")
    print(f"\033[31m3.\033[0m Delete task")
    print(f"\033[31m4.\033[0m Clear all tasks")
    print(f"\033[31m5.\033[0m Exit")

    choice = input("Choose an option:")

show_menu()


# user_input = input("Enter your tasks separated by ';':")
# new_tasks = user_input.split(";")
# tasks = load_tasks()
# tasks.extend(new_tasks)

# print("\nYour current tasks:")
# for i, task in enumerate(tasks, 1):
#     print(f"{i}) {task}")

# priority_input = input("\nDo you want to mark important tasks? (yes/no): ").lower()

# if priority_input == "yes":
#     important_tasks = input("Enter the number of important tasks separated by ',':")
#     important_numbers = [int(num) for num in important_tasks.split(",")]
    
#     if len(important_numbers) > 3:
#         important_numbers = important_numbers[:3]
#         print("You can only mark up to 3 tasks as important.")

#     for index in important_numbers:
#      tasks[index - 1] = tasks[index - 1] + "|important"

# with open("tasks.txt","w",encoding="utf-8") as file:
#     for task in tasks:
#         file.write(task + "\n")

# print("\nTasks saved successfully! 🎀")