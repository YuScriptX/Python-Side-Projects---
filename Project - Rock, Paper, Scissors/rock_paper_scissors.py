# rock , paper , scissors game

import random

game = ("rock" , "paper" , "scissors")
playing = True

while playing:

    player = None
    computer = random.choice(game)

    while player not in game:
        player = input("Make choice between rock, paper and scissors: ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    if not input("You wanna play again? (y/n): ").lower() == "y":
        break

print("Thanks for playing!")