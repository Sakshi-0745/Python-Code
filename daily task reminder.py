import time
import datetime

# Store tasks in a list of dictionaries
tasks = []

def add_task():
    task = input("Enter task: ")
    task_time = input("Enter time (HH:MM in 24-hour format): ")
    tasks.append({"task": task, "time": task_time})
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    print("\nYour Tasks:")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t['task']} at {t['time']}")

def start_reminder():
    print("Reminder started. Leave this running...")
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        for t in tasks[:]:
            if t["time"] == now:
                print(f"\nReminder: {t['task']} at {t['time']}")
                tasks.remove(t)
        time.sleep(60)

def main():
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Start Reminder")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            start_reminder()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
