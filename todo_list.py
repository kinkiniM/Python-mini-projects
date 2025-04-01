# create a to-do list program that lets users addi remove and view terms

## Function to add a task 
def add_task(task_list, task_name):
    task_list.append(task_name)
    print(f"Task '{task_name}' is added")

## Function to display the task_list
def view_task(task_list):
    if not task_list:
         print("there is no task for you today..")
    else:
         for task in task_list:
            print(f'☐ {task}')
## Function to remove tasks from task_list
def remove_task(task_list, task_name):
    if task_name in task_list:
        task_list.remove(task_name)
        print(f'Task {task_name} is removed ')
    else:
        print(f"Task {task_name} not found")

if __name__ == "__main__":
    ## initialising an Empty list
    task_list = []
    print("\n######### To-Do List ########\n")
    # Giving user options to add, remove, view and exit
    while True: #infinite loop
        print("\nEnter the operation you want to perform")
        print("\n (Add/Remove/View/Delete/Exit)")
        op = input("").strip().lower()

        if op == 'add':
            task_name = input("Add a Task:: ")
            add_task(task_list,task_name)
        elif op == 'view':
            view_task(task_list)
        elif op == 'remove':
            task_name = input("Enter the task to remove:: ")
            remove_task(task_list,task_name)
        elif op == 'exit':
            break
        else:
            print("Invalid Option, Please Try Again...")
            
## END ##