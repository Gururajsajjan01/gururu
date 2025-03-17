class BankAccount:
    def __init__(Self,balance):
        Self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficent funds")

    def get_balance(self):
        return self.__balance
    
account = BankAccount(1000)
account.deposit(499)
print(account.get_balance())
