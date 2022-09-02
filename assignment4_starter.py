# 1. Ryan Harwick
# 2. 2022-03-16
# 3. Assignment 4


supplier_data = '{"parts": ["sprocket", "gizmo", "widget", "dodad"], "sprocket": {"price": 3.99, "quantity": 32}, "gizmo": {"price": 7.98, "quantity": 2}, "widget": {"price": 14.32, "quantity": 4}, "dodad": {"price": 0.5, "quantity": 0}}'


# Your code goes here

import json

supp_dict = json.loads(supplier_data)

print("Welcome to the parts orderying system, please enter in a part name, follower by a quantity.")
print()
print("The orderable parts are:")
print("Sprocket")
print("Gizmo")
print("Widget")
print("Dodad")
print()

valid_order = 0
subTotal = 0
order = {}
order["parts"] = []

while valid_order == 0:
    user_input = input("Please enter in which part you would like to order, or quit if you are done: ")
    user_lower = user_input.lower()

    if user_lower == "quit":
        valid_order = 1

    elif user_lower not in supp_dict["parts"]:
        print("Invalid entry, please try again")
        print()

    else:
        user_quant = int(input("Please enter in the quantity for your order: "))
        act_price = supp_dict[user_lower]["price"]
        act_quantity = supp_dict[user_lower]["quantity"]

        if user_quant > act_quantity:
            print(f"Error, only", act_quantity, "of", user_lower, "are avaialble.")

        elif user_quant <= act_quantity:
            subTotal = (user_quant * act_price) + subTotal
            supp_dict[user_lower]["quantity"] = supp_dict[user_lower]["quantity"] - user_quant

            if user_lower not in order["parts"]:
                order["parts"].append(user_lower)
            
            order[user_lower] = {"quantity":user_quant,"individualPrice":act_price, "lineTotal":user_quant * act_price}

order["total"] = round(subTotal, 2)            

print()
print("Your order:")

for i in range(len(order["parts"])):
    print(f"Your item -", order["parts"][i], "with a quantity of", order[order["parts"][i]]["quantity"], "at a price of", order[order["parts"][i]]["individualPrice"], "comes to", order[order["parts"][i]]["lineTotal"])
print()
print(f"Your total comes to:", order["total"])

