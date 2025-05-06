def numberPyramid(num):

    for i in range(1, num +1):
        spaces = " " * (num - i)

        numbers = " ".join(str(j) for j in range(1, i + 1))

        print(spaces + numbers)

    for i in range(num - 1, 0, -1):
        spaces = " " * (num - i)

        numbers = " ".join(str(j) for j in range(1, i + 1))

        print(spaces + numbers)

def main():

    num = int(input("enter number here: "))
    
    numberPyramid(num)

if __name__ == "__main__":
    main()

