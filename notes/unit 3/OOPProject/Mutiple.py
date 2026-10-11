class Father:
    def skill1(self):
        print("My Father's skill is Gardening")

class Mother:
    def skill2(self):
        print("My Mother's skill is Cooking")

class Child(Father, Mother):
    def ownSkill(self):
        print("Child skill is Coding")


child = Child()
child.skill1()
child.skill2()
child.ownSkill()
