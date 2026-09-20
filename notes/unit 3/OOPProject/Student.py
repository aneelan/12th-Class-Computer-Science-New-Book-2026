class Student:
    def __init__(self, n,age):
        self.name = n
        self.age = age


    def setAge(self, age):
        self.age = age

    def display(self):
        print(f"Name:{self.name} , Age:{self.age}")

s1 = Student('Ali',20)
s2 = Student('Bob', 18)

s1.display()
s2.display()