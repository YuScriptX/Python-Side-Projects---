# Weight Converter

weight = float(input("Enter your weight: "))
unit = str(input("Kg or Lbs: "))

if unit == "Kg":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {weight} {unit}")
elif unit == "Lbs":
    weight = weight / 2.205
    unit = "Kg."
    print(f"Your weight is: {weight} {unit}")
else:
    print("Invalid value")