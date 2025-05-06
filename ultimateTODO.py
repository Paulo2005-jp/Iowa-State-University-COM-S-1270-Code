# Paulo Juarez 04-18-2025
# Assignment #5 
# This allows for the user to manage a task tracking system with stages like backlog, todo,


import sys
import pickle

def printTitleMaterial():
    print(" Ultimate TODO List!")
    print()
    print("By: Paulo Juarez")
    print("COM S 1270")
    print()

def initList():
    todoList = {
        "backlog": [],
        "todo": [],
        "in_progress": [],
        "in_review": [],
        "done": []
    }
    return todoList

def checkIfListEmpty(todoList):
    return all(len(todoList[key]) == 0 for key in todoList)

def saveList(todoList):
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "wb") as pickle_file:
            pickle.dump(todoList, pickle_file)
    except:
        print(f"ERROR (saveList): ./{listName}.lst is not a valid file name!")
        sys.exit()

def loadList():
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "rb") as pickle_file:
            todoList = pickle.load(pickle_file)
    except:
        print(f"ERROR (loadList): ./{listName}.lst was not found!")
        sys.exit()
    return todoList

def checkItem(item, todoList):
    for key in todoList:
        if item in todoList[key]:
            return True, key, todoList[key].index(item)
    return False, "", -1

def addItem(item, toList, todoList):
    itemFound, keyName, index = checkItem(item, todoList)
    if not itemFound:
        todoList[toList].append(item)
    else:
        print(f"ERROR: '{item}' already exists in {keyName} at index {index}.")
    return todoList

def deleteItem(item, todoList):
    itemFound, keyName, index = checkItem(item, todoList)
    if itemFound:
        todoList[keyName].pop(index)
    else:
        print(f"ERROR: '{item}' not found in any list.")
    return itemFound, todoList

def moveItem(item, toList, todoList):
    itemFound, todoList = deleteItem(item, todoList)
    if itemFound:
        todoList = addItem(item, toList, todoList)
    return todoList

def printTODOList(todoList):
    for key in todoList:
        print(f"{key}: {todoList[key]}")
    print()

def runApplication(todoList):
    while True:
        print("-----------------------------------------------------------------")
        choice = input("APPLICATION MENU: [a]dd to backlog, [m]ove item, [d]elete item, [s]ave list, or [q]uit to main menu?: ")
        print()
        if choice == "a":
            item = input("Enter An Item: ")
            todoList = addItem(item, "backlog", todoList)
            printTODOList(todoList)
        elif choice == "m":
            if not checkIfListEmpty(todoList):
                item = input("Enter An Item To Move: ")
                found, _, _ = checkItem(item, todoList)
                while not found:
                    print("ERROR: That item does not exist.")
                    item = input("Enter An Item To Move: ")
                    found, _, _ = checkItem(item, todoList)
                toList = input(f"Enter The List To Move {item} To: ")
                while toList not in todoList:
                    print("ERROR: That list does not exist.")
                    toList = input("Enter A Valid List Name: ")
                todoList = moveItem(item, toList, todoList)
            else:
                print("ERROR: No items to move!")
            printTODOList(todoList)
        elif choice == "d":
            if not checkIfListEmpty(todoList):
                item = input("Enter An Item To Delete: ")
                _, todoList = deleteItem(item, todoList)
            else:
                print("ERROR: No items to delete!")
            printTODOList(todoList)
        elif choice == "s":
            saveList(todoList)
            print("Saving List...")
            print()
            printTODOList(todoList)
        elif choice == "q":
            print("Returning to MAIN MENU...")
            print()
            break
        else:
            print("ERROR: Please enter [a], [m], [d], [s], or [q].")
            print()
    return todoList

def main():
    taskOver = False
    printTitleMaterial()
    while not taskOver:
        print("-----------------------------------------------------------------")
        choice = input("MAIN MENU: [n]ew list, [l]oad list, or [q]uit?: ")
        print()
        if choice == "n":
            todoList = initList()
            printTODOList(todoList)
            runApplication(todoList)
        elif choice == "l":
            todoList = loadList()
            printTODOList(todoList)
            runApplication(todoList)
        elif choice == "q":
            taskOver = True
            print("Goodbye!")
            print()
        else:
            print("Please enter [n], [l], or [q]...")
            print()

if __name__ == "__main__":
    main()
