class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

class Manager(Person, employee):
    def __init__(self, name, age, emp_id, salary):
        Person.__init__(self, name, age)  # Initialize Person attributes
        employee.__init__(self, emp_id, salary)  # Initialize employee attributes

    def display_info(self):
        print(f"Manager Name: {self.name}, Age: {self.age}, Employee ID: {self.emp_id}, Salary: {self.salary}")

Manager = Manager("Alice", 35, "M123", 75000)  # Creating an instance of Manager
Manager.display_info()  # Displaying manager's information