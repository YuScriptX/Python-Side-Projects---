# Shopping Cart Program

foods = []
prices = []
total = 0

while True:
    food = input("Enter your food name (q to quit): ").lower()
    if food == "q":
        break
    else:
        price = float(input(f"Enter the price of the {food}: € "))
        foods.append(food)
        prices.append(price)