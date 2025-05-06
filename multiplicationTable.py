

def multiplicationTable(lowNum, highNum):
   for row in range(lowNum, highNum + 1):
        for col in range(lowNum, highNum + 1):
            print(row * col, end="\t")
        print()

def main():
    lowNum = int(input("enter lowest number here: "))
    highNum = int(input("enter highest number here: "))
    multiplicationTable(lowNum, highNum)

if __name__ == "__main__":
    main()

