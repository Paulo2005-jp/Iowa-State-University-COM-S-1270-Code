#Paulo Juarez
#com s 1270


import random

def header():
    print("NIMBGRAB")
    print("BY: Paulo Juarez")

def rules():
    print("\nThe rules for this games are simple ")
    print("it starts with random items shown from 20 to 25")
    print("Players would take 1 to 3 items")
    print("The player who takes the last one looses")
    print("Now if you you choose to play with the computer")
    print("the on player mode is that the computer optimally plays")

def valid_input (prompt, minval, maxval):
    while True:
        try:
            choice = int(input(prompt))
            if minval <= choice <= maxval:
                return choice
            else:
                print(f'Error the choice you made does not exist')
        except Error:
            print("Error enter a real integer")
  

def computer_plays(items):
    return min(items, random.randint(1, 3))


def play(mode):
    items = random.randint(20, 25)
    print(f"\n The game starts with {items} sticks")

    while items > 0:
        print("sticks left:", "| " * items)

        if mode == "humanVShuman" or (mode == "humanVScomputer" and items % 2 == 1):
            take = valid_input("Choose how many sticks you'll take from 1-3: ", 1, min(3, items))
            print(f"player will take: {take}")
        else:
            take = computer_plays(items)
            print(f"computer is taking: {take}")

        items -= take

        if items == 0:
            print("\nLast stick was taken so you lost!!\n") 


def main():
    while True:
        header()
        choice = input("Do you want to [p]lay, read the [r]ules, or [q]uit?: ").lower()

        if choice == "p":
            mode = input("Do you want to play aginst a [h]uman or [c]omputer").lower()
            if mode == "h":
                play("humanVShuman")
            elif mode == "c":
                play("humanVScomputer")
            else:
                print("ERROR this coice does not exist")
        elif choice == "r":
                rules()
        elif choice == "q":
            print("See ya later :D")
            return
        else:
            print("ERROR this choice does not exist")
    
        

if __name__ == "__main__":
    main()




