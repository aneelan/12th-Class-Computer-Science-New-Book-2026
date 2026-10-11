class Vehicle:
    def start_engine(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class ElectricCar(Car):
    def charge(self):
        print("Electric car is charged")

tesla = ElectricCar()
tesla.start_engine()
tesla.drive()
tesla.charge()
