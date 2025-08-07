# Python Banking Program

def show_balance(balance):
    print(f"Show the balance: €{balance:.2f} ")

def deposit():
    amount = float(input(f"Enter your amount: "))

    if amount < 0:
        print("It is not valid")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("How much do you wanna withdraw: "))

    if amount > balance:
        print("It is invalid")
        return 0
    elif amount < 0:
        print("Still invalid, must be bigger than 0")
        return 0
    else:
        return amount


def main():

    balance = 0
    is_running = True


    while is_running:
        print("********************")
        print("Banking Program")
        print("********************")
        print("1.Show balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("********************")
        choice = input("Enter a choice between 1 & 4: ")


        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            exit("Thank you!")
        else:
            print("It is invalid")
main()