#Paulo Juarez                        2-6-2025
#coms1027

def compoundAmount(principal,rate,number_compunds,time):
    compoundAmount = principal * (1 + (rate/100) / number_compunds)**(number_compunds * time)
    return compoundAmount

def main():
    principal = float(input("enter principal: "))
    rate = float(input("enter rate: "))
    number_compunds = float(input("enter number compunds: "))
    time = float(input("enter time: "))
    answer = compoundAmount(principal,rate,number_compunds,time)
    print("compund amount: ", answer)

if __name__ == "__main__":
    main()
    