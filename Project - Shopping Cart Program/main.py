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

print("----- YOUR CART -----")

for food in foods:
    print(food)

for price in prices:
    print(price)