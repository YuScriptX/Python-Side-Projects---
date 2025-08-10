# Slot Machine

import random

def spin_row():
    symbols = ['🍉', '🍋', '🍒', '⭐']

    results = []

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" ".join(row))

def get_payout():
    pass

def main():
    balance = 1000

    print("/****** Welcome to the game! ******/")
    print("Symbols : 🍉 🍋 🍒 ⭐")
    print("/*************************/")

    while balance > 0:
        print(f"Your balance is: € {balance}")

        bet = input("How much you wanna bet: ")

        if not bet.isdigit():
            print("Enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("It is bigger than your balance")
            continue

        if bet <= 0:
            print("It must be bigger than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)
        

if __name__ == '__main__':
    main()