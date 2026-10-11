class Calcuator:
    def multipy(self,a=1,b=1, *args):
        result = a * b

        for i in args:
            result *= i

        return result

calc = Calcuator()
print(calc.multipy())
print(calc.multipy(2))
print(calc.multipy(3,4))
print(calc.multipy(3,4,5,2))