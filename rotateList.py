def get_list():
    intlist = []
    while True:
        user = input("Enter a number or (-)to stop: ")
        if user == "-":
            break
    try:
        number = int(user)
        intlist += [number]
    except ValueError:
        print("ERROR enter a number!!")
    return intlist

def rotatelist(lst, rot):
    if not lst:
        return []
        
    n = len(lst)
    rot = rot % n if rot >= 0 else -(abs(rot) % n)

    if rot == 0:
        return lst
    elif rot > 0:
        return lst[-rot:] + lst[:-rot] if rot else lst
        
    else:
        rot = abs(rot) % n
        return lst[-rot:] + lst[:-rot]

def main():
    intlist = get_list()

    #if not intlist:
     #   print("empty!!")
      #  return

    try:
        rot = int(input("enter rotation number: "))
    except ValueError: 
        print("bad rotation input")   
        return

    rotated = rotatelist(intlist, rot)
    print("ROtated list: ", rotated)

if __name__ == "__main__":
    main()