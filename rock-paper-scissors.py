import random
name = input("What is your name? \n")
print(name, "Welcome to my rock, paper, scissors game. ")

player_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    player_input = input("Choose one between Rock, Paper, Scissors or Q to quit:\n").lower()
    if player_input == "q":
        break
    

    if player_input not in options:
        print("Input is invalid!")
        continue
    
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if player_input == "rock" and computer_pick == "scissors":
        print("You won!")
        player_wins += 1
        continue
    elif player_input == "paper" and computer_pick == "rock":
        print("You won!")
        player_wins += 1
    elif player_input == "scissors" and computer_pick == "paper":
        print("You won!")
        player_wins += 1
    else:
        print("You lost!")
        computer_wins += 1


print("You won", player_wins, "times.")
print("The computer won", computer_wins, "times.")




