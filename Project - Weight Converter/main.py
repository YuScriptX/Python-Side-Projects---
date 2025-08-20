# Weight Converter

weight = float(input("Enter your weight: "))
unit = str(input("Kg or Lbs: "))

if unit == "Kg":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "Lbs":
    weight = weight / 2.205
    unit = "Kg."
else:
    print("Invalid value")

print(f"Your weight is: {weight} {unit}")