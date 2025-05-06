
# Author: Paulo Juarez
# Date: 2025-04-22
# Lab: Rock Paper Scissors with Test Driven Development
# Description: A simple implementation of Rock, Paper, Scissors using TDDo

import random

def generateComputerMove():
    return random.choice(["Rock", "Paper", "Scissors"])



def determineWinner(playerMove, computerMove):
    if playerMove == computerMove:
        return "its a Draw"
    wins = {
        ("Rock", "Scissors"),
        ("Paper", "Rock"),
        ("Scissors", "Paper")
    }
    if (playerMove, computerMove) in wins:
        return playerMove
    else:
        return computerMove

def playRound(playerMove):
    computerMove = generateComputerMove()
    winner = determineWinner(playerMove, computerMove)
    if winner == "Draw":
        return "Draw"
    elif winner == playerMove:
        return "You Win"
    else:
        return "Computer Won!!"

def main():
    print("Welcome to Rock Paper Scissors")
    while True:
        try:
            rounds = int(input("Enter an odd number of rounds to play: "))
            if rounds % 2 == 1:
                break
            else:
                print("Number must be odd.")
        except ValueError:
            print("Invalid input.")

    playerWins = 0
    computerWins = 0
    neededWins = rounds // 2 + 1

    while playerWins < neededWins and computerWins < neededWins:
        playerMove = input("Choose Rock, Paper, or Scissors: ").capitalize()
        if playerMove not in ["Rock", "Paper", "Scissors"]:
            print("Invalid move.")
            continue
        result = playRound(playerMove)
        print(result)
        if result == "You Win!":
            playerWins += 1
        elif result == "Computer Wins!":
            computerWins += 1
        print(f"Score - You: {playerWins}  Computer: {computerWins}")

    print("Game Over")
    if playerWins > computerWins:
        print("You are the champion!")
    else:
        print("Computer is the champion")

if __name__ == "__main__":
    main()
