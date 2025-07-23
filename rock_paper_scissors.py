# rock , paper , scissors game

import random

game = ("rock" , "paper" , "scissors")
player = None
computer = random.choice(game)


player = input("Make choice between rock, paper and scissors: ")

print(f"Player: {player}")
print(f"Computer: {computer}")

