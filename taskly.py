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