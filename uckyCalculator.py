#Paulo Juarez        02/20/2025
#coms 1027 luckyCalculator

import random

def luckyCalculator():

    a = int(input("enter integer: "))
    b = int(input("enter integer: "))
    calculation = input("Please enter integer calculation type [+], [-], [*], [/], [//], [%], [**]:")

if calculation not in ['+', '-', '*', '/', '//', '%', '**']:
    print("ERROR you must enter one of these '+', '-', '*', '/', '//', '%', '**'")
    return 

if calculation in ['/', '//', '%'] and b == 0:
    print(f"ERROR in {calculation} function: b = 0")
    print(f'The result pf your calculation was: {a}')
    return

if calculation == '+':
    result = a + b
elif calculation == '*':
    result = a * b
elif calculation == '-':
    result = a - b
elif calculation == '/':
    result = a / b
elif calculation == '//':
    result = a // b
elif calculation == '%':
    result = a % b
elif calculation == '**':
    result = a ** b

print(f"The result is: {result}")

def luckynumber():
    a = int(input("enter integer: "))
    b = int(input("enter integer: "))
    number = random.randint(a, b)
    print(f"the lucky number is: {number}")

def main():
    print("Lucky Calculator")
    print("Author: Paulo Juarez")
    print("COMS 1270")
    print("choos your calculation type: ")

    operand = input("[c]calculator, [l]lucky, [q]uit")
    if operand == 'c':
        calculator()
    elif operand == 'l':
        luckynumber()
    elif operand == 'q':
        print("Goodbye ;)")
    else:
        print('ERROR: try again')




