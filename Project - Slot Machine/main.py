# Slot Machine

import random

def spin_row():
    symbols = ['🍉', '🍋', '🍒', '⭐']

    results = []

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍉':
            return bet * 5
        elif row[0] == '🍋':
            return bet * 8
        elif row[0] == '🍒':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 100
    return 0        

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

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won! €{payout}")
        else:
            print("You lose!")

        balance += payout

        play_again = str(input("Do you wanna play again? (Y/N): ")).upper()

        if not play_again == 'Y':
            break

    print(f"Thank you for playing, you're balance is €{balance}")

if __name__ == '__main__':
    main()