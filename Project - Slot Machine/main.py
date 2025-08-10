# Slot Machine

def spin_row():
    pass

def print_row():
    pass

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

if __name__ == '__main__':
    main()