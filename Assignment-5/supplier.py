# 1. Ryan Harwick
# 2. 2022-03-28
# 3. Assignment 5 - supplier.py

class Supplier:

    def __init__(self, name):
        self.name = name
        self.parts = {}
        self.parts[self.name+"_parts"] = []

    def add_part(self, part, price):
        self.parts[self.name+"_parts"].append(part)
        self.parts[self.name+"_"+part+"_price"] = price

    def price_check(self, part):
        price = self.parts[self.name+"_"+part+"_price"]
        return price

    def check_supply(self, part):
        
        if part in self.parts[self.name+"_parts"]:
            isAvailable = True
        else:
            isAvailable = False

        return isAvailable