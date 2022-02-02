# 1. Ryan Harwick
# 2. 2022-02-01
# 3. Assignment 2

table_order = ["Pasta Bolognere", "Pasta Carbonara", "Salad", "Diet Coke", "Sprite"]
menu_prices = [10.99, 11.99, 2.99, 1.99, 1.99]

subTotal = 0

print("Good Food Served Here\nReceipt\n")

for food, price in zip(table_order, menu_prices):
    print(f"{food} - {price}")
    subTotal = subTotal + price

printSub = round(subTotal, 2)
print(f"\nSubtotal: {printSub}")

tax = round(printSub * 0.0625, 2)

print(f"Tax (6.25%): {tax}")

total = printSub + tax

print(f"Grand Total: {total}")

print("\nThank you for buying our food!")