#Paulo Juarez                        2-6-2025
#coms1027

def studentLoanAmortization (principal, yearlyInterestRate, numberOfYears):
    
    monthlyInterestRate = yearlyInterestRate / 12

    numberOfMonths = numberOfYears * 12

    monthlyPayment = (monthlyInterestRate * principal) / (1-(1 + monthlyInterestRate) ** -numberOfMonths)

    print("\n Amortization Schedule")
    print(f"{'Period':<8}{"Total Payment Due":<20}{"Interest Due":<25}{"Principal Due":<25}{"BALANCE:":<20}")
    print("--------------------------------------------------------------------------------------")

    remainingBalance = principal

    for period in range(1, numberOfMonths + 1):
        interestDue = remainingBalance * monthlyInterestRate
        principalDue = monthlyPayment - interestDue
        remainingBalance -= principalDue

        if remainingBalance < 0:
            remainingBalance = 0

        print(f'{period:<8}{monthlyPayment:<20.2f}{interestDue:<25.2f}{principalDue:<20.2f}{remainingBalance:<20.2f}')
        
    print("-----------------------------------------------------------------------")
    print(f"Total Paid: {monthlyPayment * numberOfMonths:.2f}")

def main():
    try:
        principal = float(input("ENter the principal amount: "))
        yearlyInterestRate = float(input("enter yearly interest rate: "))
        numberOfYears = int(input("enter number of the years: "))
        studentLoanAmortization(principal, yearlyInterestRate, numberOfYears)
    except ValueError:
        print("error try again")
        

if __name__ == "__main__":
    main()
