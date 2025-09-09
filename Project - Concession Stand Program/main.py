# Concession Stand Program

menu = {"soda": 3.00,
        "nachos": 5.00,
        "chips": 7.00,
        "hotdog": 9.00,
        "kebab": 12.00,
        "pizza": 15.00,}

cart = []
total = 0

print("----- MENU -----")
for key, value in menu.items():
    print(f"{key:10}: €{value:.2f}")
print("----------------")

while True:
    food = input("Select a item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print(cart)