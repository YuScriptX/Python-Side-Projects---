# Weight Converter

weight = float(input("Enter your weight: "))
unit = str(input("Kg or Lbs: "))

if unit == "Kg":
    weight = weight * 2.205
elif unit == "Lbs":
    weight = weight / 2.205
else:
    print("Invalid value")

print(f"Your weight is: {weight} {unit}")