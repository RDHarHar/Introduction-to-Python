# 1. Ryan Harwick
# 2. 2022-03-28
# 3. Assignment 5 - database.py

import supplier

class Database:

    def __init__(self):
        self.data = []
    
    def add_supplier(self, name):
        self.data.append({"name": name})

    def find_part(self, part):
        #  ╔═══╗
        #  ║╔═╗║
        #  ╚╝╔╝║
        #    ║╔╝
        #    ╔╗
        #    ╚╝