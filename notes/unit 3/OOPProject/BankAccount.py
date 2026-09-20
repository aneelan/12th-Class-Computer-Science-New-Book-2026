class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):

        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Yours balance is insufficient")

    def getBalance(self):
        return self.__balance

bankAccount = BankAccount(1000)
print("Balance: ",bankAccount.getBalance())

bankAccount.deposit(500)
print("Balance: ",bankAccount.getBalance())

bankAccount.withdraw(700)
print("Balance: ",bankAccount.getBalance())

bankAccount.withdraw(1000)
print("Balance: ",bankAccount.getBalance())
