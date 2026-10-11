
# Base Class (Parent Class)
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} is starting...")

    def stop(self):
        print(f"{self.brand} {self.model} has stopped.")

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")


# Subclass 1: Car (inherits from Vehicle)
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model) # Call parent constructor
        self.doors = doors

    # Unique method for Car
    def open_trunk(self):
        print(f"{self.brand} {self.model}'s trunk is now open.")

    def display_info(self): # Method Overriding
        super().display_info()
        print(f"Number of Doors: {self.doors}")
# Subclass 2: Bike (inherits from Vehicle)
class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    # Unique method for Bike
    def wheelie(self):
        print(f"{self.brand} {self.model} is doing a wheelie!")

    def display_info(self): # Method Overriding
        super().display_info()
        print(f"Engine Capacity: {self.engine_cc} cc")
# ========== Demonstration ==========
print("----- Car Object -----")
my_car = Car("Toyota", "Corolla", 4)
my_car.start() # Inherited method
my_car.open_trunk() # Unique method of Car
my_car.display_info() # Overridden method
my_car.stop() # Inherited method
print("\n----- Bike Object -----")
my_bike = Bike("Honda", "CG-125", 125)
my_bike.start() # Inherited method
my_bike.wheelie() # Unique method of Bike
my_bike.display_info() # Overridden method
my_bike.stop() # Inherited method