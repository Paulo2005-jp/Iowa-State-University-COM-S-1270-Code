#Paulo Juarez                        2-6-2025
#coms1027
#reference: https://www.geeksforgeeks.org/python-program-to-calculate-acceleration-final-velocity-initial-velocity-and-time/

def velocityAccelerationTime(fv,acc,time):

    finalVelocity = fv + (acc * time)
    return finalVelocity

def main():
     fv = float(input("enter final velocity: "))
     acc = float(input("enter acceleration: "))
     time = float(input("enter time: "))
     answer = velocityAccelerationTime(fv,acc,time)
     print("the answer is", answer)

if __name__ == "__main__":
    main()





