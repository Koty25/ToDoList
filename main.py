
def printLists(yourList): #TODO: implement with dictionaries instead of lists
    viewList = [item.strip("\n") for item in yourList]
    for item in viewList:
        if isinstance(item, list):
            printLists(item)
        elif isinstance(item, str):
            print(f"{viewList.index(item)}. {item}")

userName = input("Enter your name: ")

taskListName = ("tasklist" + userName + ".txt")
try:
    with open(taskListName, "r") as file:
        taskList = file.readlines()
except FileNotFoundError:
    with open(taskListName, "w") as file:
        file.writelines(userName + "'s ToDo list\n")
    with open(taskListName, "r") as file:
        taskList = file.readlines()
    print(f"Hi, {userName}. Welcome to your ToDo list")
    print(f"If this is your first time using this ToDo program, here is a how to use it:")
    print(f"You can type the number of the action you want to do;")
    print(f"or, you can type the action + the input you want to insert. For example: add clean dishes; or edit 1 clean all dishes; view.")
    print(f"These are some examples. Type help to see all possible actions.")

while True:
    print("----------------------")
    print("1. Add task")
    print("2. Edit tasks")
    print("3. View tasks")
    print("4. Complete task")
    print("5. Child task")
    print("6. Exit")
    print("----------------------")
    userAction = input("Enter the action's number: ")
    if userAction == "help":
        print(f"to do help section")
        break
    try:
        if int(userAction).is_integer():
            actionMode = 1
    except ValueError:
        actionMode = 0

    if actionMode == 1:
        userAction = int(userAction)
        match userAction:
            case 1:
                print("Add task")
                taskList.append("[ ]" + input("Enter task to add: ") + "\n")
                with open(taskListName, "w") as file:
                    file.writelines(taskList)
            case 2:
                print("Edit tasks")
                print("Tasks: ")
                viewTaskList = [item.strip("\n") for item in taskList]
                for item in viewTaskList:
                    print(f"{viewTaskList.index(item)}. {item}")
                task2Edit = int(input("Enter task number to edit: "))
                taskList[task2Edit] = ("[ ]" + input("Enter new task: ") + "\n")
                with open(taskListName, "w") as file:
                    file.writelines(taskList)
            case 3:
                print("View tasks")
                printLists(taskList)
            case 4:
                print("Complete task (Completed tasks are removed in 8 hours)")
                print("Tasks: ")
                viewTaskList = [item.strip("\n") for item in taskList]
                for item in viewTaskList:
                    print(f"{viewTaskList.index(item)}. {item}")
                taskList.pop(int(input("Enter task number to complete: ")))
                with open(taskListName, "w") as file:
                    file.writelines(taskList)
                break
            case 5:
                print("Add Child task")
                print("Tasks: ")
                viewTaskList = [item.strip("\n") for item in taskList]
                for item in viewTaskList:
                    print(f"{viewTaskList.index(item)}. {item}")
                task2Edit = int(input("Enter task number to add a child task: "))
                print("todo") #TODO: implement with dictionaries instead of lists
                #taskList[task2Edit] = input("Enter note: ")
            case 6:
                print("Exit, até logo!")
                break
            case _:
                print("Invalid choice")
    elif actionMode == 0:
        if userAction.startswith("add"):
            print("Add task")
            taskList.append("[ ]" + userAction[4:] + "\n")
            with open(taskListName, "w") as file:
                file.writelines(taskList)
        elif userAction.startswith("edit"):
            print("Edit tasks")
            print("Tasks: ")
            taskList[int(userAction[5])] = ("[ ]" + userAction[7:] + "\n")
            with open(taskListName, "w") as file:
                file.writelines(taskList)
            viewTaskList = [item.strip("\n") for item in taskList]
            for item in viewTaskList:
                print(f"{viewTaskList.index(item)}. {item}")
            continue
        elif userAction.startswith("view"):
            print("View tasks")
            printLists(taskList)
            continue
        elif userAction.startswith("complete"):
            print("Complete task (Completed tasks are removed in 8 hours)")
            taskList.pop(int(userAction[9]))
            with open(taskListName, "w") as file:
                file.writelines(taskList)
            print("to do 8 hour completion + left side marker")
            viewTaskList = [item.strip("\n") for item in taskList]
            for item in viewTaskList:
                print(f"{viewTaskList.index(item)}. {item}")
            continue
        elif userAction.startswith("child"):
            print("Add Child task")
            task2Note = int(userAction[5])
            print("todo") #TODO: implement with dictionaries instead of lists
            print("Tasks: ")
            viewTaskList = [item.strip("\n") for item in taskList]
            for item in viewTaskList:
                print(f"{viewTaskList.index(item)}. {item}")
            #taskList[task2Edit] = input("Enter note: ")
            continue
        elif userAction.startswith("exit"):
            print("Exit, até logo!")
            continue
        else:
            print("Invalid choice")
            continue
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
