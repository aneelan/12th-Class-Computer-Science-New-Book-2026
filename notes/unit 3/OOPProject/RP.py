class Animal:
    def sound(self):
        return "Sound of animal"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"


animals = [Dog(),Cat(),Animal()]

for animal in animals:
    print(animal.sound())

animal = Animal()
print("Animal :",animal.sound())

animal = Dog()
print("Dog :",animal.sound())

animal = Cat()
print("Cat :",animal.sound())