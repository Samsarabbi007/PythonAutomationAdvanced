
''' class className:
  def __init__(self, name, age):
        self.name = name
        self.age = age
--init-- is a constructor method that initializes the object with name and age attributes.
self is a reference to the current instance of the class.

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
 '''


class Person:
    def __init__(self, name, id):
        self.name = name  # Instance variable for name
        self.id = id   # Instance variable for ID

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.id}")  # Method to display person's details

#Create an instance of the Person class
person1 = Person("Alice", 101)  # Creating an object of Person class with name and ID
person2 = Person("Bob", 102)
person1.display_info()
person2.display_info()  # Displaying information of person2