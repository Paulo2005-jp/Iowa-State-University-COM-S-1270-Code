# Paulo Juarez 2025-05-06
# Lab: FizzBuzz with Modulus and Dictionary Methods
# This script takes a user input integer and solves the 'FizzBuzz' problem up to that number
# using two different methods: modulus and dictionary-based logic. It also prints "Bazz" for
# numbers divisible by 7.

def fizzBuzzModulus(n):
    result = []
    for i in range(1, n + 1):
        entry = ""
        if i % 3 == 0:
            entry += "Fizz"
        if i % 5 == 0:
            entry += "Buzz"
        if i % 7 == 0:
            entry += "Bazz"
        result.append(entry if entry else str(i))
    return result

def fizzBuzzDict(n):
    result = []
    fb_dict = {3: "Fizz", 5: "Buzz", 7: "Bazz"}
    for i in range(1, n + 1):
        entry = "".join(word for key, word in fb_dict.items() if i % key == 0)
        result.append(entry if entry else str(i))
    return result

def main():
    try:
        num = int(input("Enter an integer: "))
        print("\n--- fizzBuzzModulus Output ---")
        print(fizzBuzzModulus(num))
        print("\n--- fizzBuzzDict Output ---")
        print(fizzBuzzDict(num))
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
