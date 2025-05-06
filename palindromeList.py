
def get_name():
    palList= []
    while True:
        user = input("Enter a string then (-) to end: ")
        if user == "-":
            break
        palList.append(user)
    return palList

def palindromeList(palList):
    for i in range(len(palList) // 2):
        if palList[i] != palList[len(palList) - 1 - i]:
            return False 
        return True

if __name__ == "__main__":
    palList = get_name()
    result = palindromeList(palList)
    print("List typed: ", palList)
    print("is this Palindrome??", result)