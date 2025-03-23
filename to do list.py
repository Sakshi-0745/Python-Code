todo_list=[]
def add_task(task):
    todo_list.append(task)
    print(f"task '{task}' added successfully")
def remove_task(task):
    todo_list.remove(task)
    print(f"task '{task}' removed successfully")
def view_list():
    print(todo_list)
while True:
    user_choice=input("enter your choice: add, remove, view, exit:")
    if user_choice=="add":
        task=input("enter the task:")
        add_task(task)
    elif user_choice=="remove":
        task=input("enter task to remove:")
        remove_task(task)
    elif user_choice=="view":
        view_list()
    elif user_choice=="exit":
        print("goodbye")
        break
    else:
        print("invalid choice")
        