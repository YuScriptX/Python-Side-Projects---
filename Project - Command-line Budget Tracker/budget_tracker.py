# Budget Tracker
# Een eenvoudige command-line budget tracker in Python
# Functies: inkomsten en uitgaven bijhouden, balans tonen, transacties weergeven

# Lijst om alle inkomensbedragen op te slaan
income_list = []

# Lijst om uitgaven op te slaan als dictionaries met bedrag en categorie
expense_list = []

# # Functie om een inkomen toe te voegen
def add_income():
    amount = float(input("Voer het bedrag in van je inkomen: €"))
    income_list.append(amount)
    print(f"Inkomen van €{amount:.2f} toegevoegd.")

# Functie om een uitgave toe te voegen, inclusief categorie
def add_expense():
    amount = float(input("Voer het bedrag in van je uitgave: €"))
    category = input("Voer categorie in (bijv. huur, auto, etc.): ")
    expense_list.append({"bedrag": amount, "categorie": category})
    print(f"Uitgave van €{amount:.2f} voor {category} toegevoegd.")

# Functie om de balans te tonen: totaal inkomen - totaal uitgaven
def show_balance():
    total_income = sum(income_list)
    total_expense = sum([item["bedrag"] for item in expense_list])
    balance = total_income - total_expense

    print("\n--- Overzicht ---" )
    print(f"Totaal inkomen: €{total_income:.2f}")
    print(f"Totaal uitgaven: €{total_expense:.2f}")
    print(f"Saldo           :€{balance:.2f}")
    print("-----------------\n")

# Functie om een overzicht van alle transacties te tonen
def show_transactions():
    print("\n--- Inkomsten ---")
    for i, income in enumerate(income_list, 1):
        print(f"{i}. €{income:.2f}")

    print("\n--- Uitgaven ---")
    for i, expense in enumerate(expense_list, 1):
        print(f"{i}. €{expense["bedrag"]:.2f} - {expense["categorie"]}")
    print()

# ------------------------------------
# Menu: Hoofdmenu van het programma
# ------------------------------------

def menu():
    while True:
        # Menuopties tonen
        print("***** Budget Tracker *****")
        print("1. Inkomen toevoegen")
        print("2. Uitgave toevoegen")
        print("3. Toon balans")
        print("4. Toon alle transacties")
        print("5. Exit")
        print("**************************")

        # Gebruiker moet een keuze maken
        choice = input("Maak een keuze (1 - 5): ")

        # Koppel keuzes aan functies
        if choice == '1':
            add_income()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            show_balance()
        elif choice == '4':
            show_transactions()
        elif choice == '5':
            exit("Dank u!")
        else:
            print("Verkeerde keuze, kies tussen 1 & 5 ")

menu() 