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
    show_balance = total_income - total_expense

    print("\n--- Overzicht ---" )
    print(f"Totaal inkomen: €{total_income:.2f}")
    print(f"Totaal uitgaven: €{total_expense:.2f}")
    print(f"Saldo           :€{show_balance:.2f}")
    print("-----------------\n")