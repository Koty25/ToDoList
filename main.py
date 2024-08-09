# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def printHi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}. Welcome to your ToDo list')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    userName = input("Enter your name: ")
    printHi(userName)

file = open("tasklist.txt", "r")
taskList = file.readlines()
file.close()

while True:
    print("1. Add task")
    print("2. Edit tasks")
    print("3. View tasks")
    print("4. Remove task")
    print("5. Add Note to task")
    print("6. Exit")
    userAction = int(input("Enter your choice: "))
    match userAction:
        case 1:
            print("Add task")
            taskList.append(input("Enter task to add: ") + "\n")
            file = open("tasklist.txt", "w")
            file.writelines(taskList)
            file.close()
        case 2:
            print("Edit tasks")
            print("Tasks: ")
            for item in taskList:
                print(f"{taskList.index(item)}. {item}")
            task2Edit = int(input("Enter task number to edit: "))
            taskList[task2Edit] = input("Enter new task: ")
        case 3:
            print("View tasks")
            for item in taskList:
                print(f"{taskList.index(item)}. {item}")
        case 4:
            print("Complete task (Completed tasks are removed in 8 hours)")
            print("Tasks: ")
            for item in taskList:
                print(f"{taskList.index(item)}. {item}")
            taskList.pop(int(input("Enter task number to complete: ")))
            break
        case 5:
            print("Add Note to task")
            print("Tasks: ")
            for item in taskList:
                print(f"{taskList.index(item)}. {item}")
            task2Edit = int(input("Enter task number to edit: "))
            print("to do")
            #taskList[task2Edit] = input("Enter note: ")
        case 6:
            print("Exit, até logo!")
            break
        case _:
            print("Invalid choice")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
