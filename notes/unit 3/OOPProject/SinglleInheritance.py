class Animal:
    def __init__(self,name):
        self.name=name

    def eat(self):
        print(f"{self.name} is Eating")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!!")

    def eat(self):
        super().eat()
        print(f"My {self.name} likes meat.")


dog = Dog("Buddy")
dog.eat()
dog.bark()
