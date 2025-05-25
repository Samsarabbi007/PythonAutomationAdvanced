class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.id}")

class Student(Person):
    def __init__(self, name, id, grade):
        super().__init__(name, id)  # Call the constructor of the parent class
        self.grade = grade  # Additional attribute for Student

    def display_info(self):
        super().display_info()  # Call the parent class method
 #       print(f"Grade: {self.grade}")  # Display additional information for Student
        print(f"Student {self.name} with ID {self.id} is in grade {self.grade}.")
# This code demonstrates single inheritance in Python.
# The Student class inherits from the Person class, allowing it to use its methods and attributes.
# The Student class adds an additional attribute 'grade' and overrides the display_info method to include it.

# Create an instance of the Student class
student1 = Student("Alice", 101, "A")  # Creating an object of Student class with name, ID, and grade
student1.display_info()