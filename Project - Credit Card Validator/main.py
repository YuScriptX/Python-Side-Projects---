# Credit card validator program

sum_odd_digits = 0
sum_even_digits = 0
total = 0

card_number = input("Enter a credit card #: ")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
card_number = card_number[::-1]

for x in card_number[::2]:
    sum_odd_digits += int(x)

print(sum_odd_digits)

