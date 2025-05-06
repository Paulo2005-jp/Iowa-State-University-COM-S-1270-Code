# Paulo Juarez - 2025-04-29
# COM S 1270 

import random


COLORS = ["R", "G", "B", "Y", "M", "C"]
BOARD = ["START", "M", "R", "B", "M", "C", "G", "B", "Y", "C", "B", "G", "Y", "G", "C", "Y", "R", "M", "R", "GOAL"]



def create_deck(copies):
    return random.sample(COLORS * copies, k=len(COLORS) * copies)

def display_board(positions):
    for i, space in enumerate(BOARD):
        print(f"{i:2} {space}", end=" | ")
        for idx, pos in enumerate(positions):
            if pos == i:
                print(f"P{idx+1}", end="")
        print()

def next_position(board, color, current_pos):
    for i in range(current_pos + 1, len(board)):
        if board[i] == color:
            return i
    return current_pos  

def player_action(name, is_human, deck):
    if is_human:
        while True:
            try:
                action = input(f"{name}: [d]raw, [s]huffle, [q]uit: ").lower()
                if action == "d":
                    card = deck.pop(0)
                    print(f"{name} drew: {card}")
                    return card
                elif action == "s":
                    random.shuffle(deck)
                    print(f"{name} shuffled the deck!")
                    return None
                elif action == "q":
                    print("Quitting")
                    exit()
                else:
                    print("Error!!!")
            except Exception as e:
                print("Error:", e)
    else:
        card = deck.pop(0)
        print(f"{name} drew: {card}")
        return card

def play_game():
    while True:
        try:
            num_humans = int(input("How many human players [1-4]? "))
            if 1 <= num_humans <= 4:
                break
            else:
                print("Must be between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")

    total_players = 4
    players = [{"name": f"Player {i+1}", "pos": 0, "is_human": i < num_humans} for i in range(total_players)]

    while True:
        try:
            copies = int(input("How many copies of each card [1-5]? "))
            if 1 <= copies <= 5:
                break
            else:
                print("Must be between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")

    deck = create_deck(copies)
    game_over = False

    while not game_over:
        display_board([p["pos"] for p in players])
        for p in players:
            input("Press ENTER to continue...")
            action = player_action(p["name"], p["is_human"], deck)
            if action:
                new_pos = next_position(BOARD, action, p["pos"])
                print(f"{p['name']} moves from {p['pos']} to {new_pos}")
                p["pos"] = new_pos
                if BOARD[new_pos] == "GOAL":
                    print(f"{p['name']} WINS! ")
                    game_over = True
                    break


def show_instructions():
    print("""
    Candy Realm Instructions:
    - so 4 players take turns drawing color cards.
    - Each card lets the player move to the next space of that color.
    - First to reach the GOAL wins
    - Shuffle the deck
    """)

def main():
    print("Candy Realm")
    print("By: Paulo Juarez")
    print("COM S 1270")
  ##print("-" * 60)

    while True:
        choice = input("MAIN MENU: [p]lay game, [i]nstructions, [q]uit: ").lower()
        if choice == "p":
            play_game()
        elif choice == "i":
            show_instructions()
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
