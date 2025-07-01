def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
               return[line.strip() for line in f.readlines()]
    except FileNotFoundError :
        return[]
       
def save_tasks(tasks):
    with open("tasks.txt","w")as f:
       for task in tasks:
           f.write(task + "\n")

def add_tasks(tasks): 
    task =input("enter the task here: ")
    tasks.append(task)
    print("task added succesfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")
        

def delete_tasks(tasks):
    view_tasks(tasks)
    try:
        num=int(input("enter task number to delete"))
        removed =tasks.pop(num-1)
        print(f"Deleted: {removed}")
    except:
         print("invalid input")
def main():
    tasks =load_tasks()
    while  True:
        print("\n ------- TO-DO LIST MENU------\n")
        print("1.View Tasks")
        print("2. Add Tasks")
        print("3. Delete Tasks")
        print("4. Exit")
        choice =input("enter your choice here(1-4):")

        if choice =='1':
            view_tasks(tasks)
        elif choice =='2':
            add_tasks(tasks)
        elif choice =='3':
            delete_tasks(tasks)
        elif choice =='4':
            save_tasks(tasks)
            print("Tasks Saved. Goodbye!")
            break
        else:
            print("invalid choice.Try Again!")


main()













