# Question 1

class Employees:
    def __init__(self):
        self.data = []
        
    def add_employee(self, name, age, title):
        self.data.append({"name": name, "title": title, "age": age})

    def print_employees(self):
        for employee in self.data:
            print(f"{employee['name']} – {employee['title']}")

    def employee_count(self):
        return len(self.data)

    def update_employee(self, name, age, title):
        for employee in self.data:
            if employee["name"] == name:
                employee["age"] = age
                employee["title"] = title