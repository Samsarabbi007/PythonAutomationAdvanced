class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class employee:
    def __init__(self, name,emp_id,):
        self.name = name
        self.emp_id = emp_id


class Manager(employee):
    def __init__(self, name,emp_id, department):
        employee.__init__(self, emp_id)  # Initialize employee attributes
        self.department = department

class Director(Manager):
    def __init__(self, name, emp_id, department, region):
        Manager.__init__(self, name, emp_id, department)  # Initialize Manager attributes
        self.region = region  # Additional attribute for Director

    def display_info(self):
        print(f"Director Name: {self.name}, Employee ID: {self.emp_id}, Department: {self.department}, Region: {self.region}")

        # Displaying information for Director

Director=Director(name="John", emp_id=101, department="Sales", region="North")  # Creating an instance of Director

Director.display_info()
