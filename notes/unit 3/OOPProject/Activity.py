class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} is starting...")

    def stop(self):
        print(f"{self.brand} {self.model} is stopping...")

    def display(self):
        print(f"{self.brand} {self.model} is displaying...")

class Car(Vehicle):
    def __init__(self, brand, model, door):
        super().__init__(brand, model)
        self.door = door

    def hasTrunk(self):
        print(f"{self.brand} {self.model} has a trunk...")

    def display(self):
        super().display()
        print(f"{self.brand} {self.model} has {self.door} doors...")

class Bike(Vehicle):
    def __init__(self, brand, model, engine):
        super().__init__(brand, model)
        self.engine = engine

    def wheelie(self):
        print(f"{self.brand} {self.model} is doing a wheelie!")

    def display(self):
        super().display()
        print(f"{self.brand} {self.model} has {self.engine} engine...")


car = Car("Toyota", "Corolla",4)
car.start()
car.hasTrunk()
car.stop()
car.display()

bike = Bike("Honda","CG-125", 125)
bike.start()
bike.wheelie()
bike.stop()
bike.display()