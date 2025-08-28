# Compound Interest Calculator

principle = 0
rate = 0
time = 0

while principle <=0:
    principle = float(input("Enter the principle amount:"))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")

print(principle)