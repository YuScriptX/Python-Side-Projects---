# Python Banking Program

def show_balance():
    pass

def deposit():
    pass

def withdraw():
    pass

balance = 0
is_running = True

while is_running:
    print("1.Show balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = input("Enter a choice between 1 & 4: ")

    if choice == '1':
        show_balance()
    elif choice == '2':
        balance()
    elif choice == '3':
        deposit()
    elif choice == '4':
        withdraw()
    else:
        print("It is invalid")