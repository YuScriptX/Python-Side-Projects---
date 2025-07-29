# Budget Tracker
# Een eenvoudige command-line budget tracker in Python
# Functies: inkomsten en uitgaven bijhouden, balans tonen, transacties weergeven

# Lijst om alle inkomensbedragen op te slaan
income_list = []

# Lijst om uitgaven op te slaan als dictionaries met bedrag en categorie
expense_list = []

# Functie om een inkomen toe te voegen
def add_income():
    amount = float(input("Voer het bedrag in van je inkomen: €"))
    income_list.append(amount)
    print(f"Inkomen van €{amount:.2f} toegevoegd.")