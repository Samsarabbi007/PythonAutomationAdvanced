class Vchicle:
    def __init__(self, model, year):
        self._model = model#
        self._year = year  # Protected member

class Car(Vchicle):
    def __init__(self, model, year, speed):
        super().__init__(model, year)  # Initialize Vchicle attributes
        self._speed = speed  # Protected member

    def display_info(self):
        print(f"Car Model: {self._model}, Year: {self._year}, Speed: {self._speed}")


Car = Car("Toyota", 2020, 1000)  # Creating an instance of Car
Car.display_info()  # Displaying information for Car

class Truck:
    def __init__(self, model, year, capacity):
        self._model = model  # Protected member
        self._year = year  # Protected member
        self._capacity = capacity  # Protected member

    def display_info(self):
        print(f"Truck Model: {self._model}, Year: {self._year}, Capacity: {self._capacity} tons")
