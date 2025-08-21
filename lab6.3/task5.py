class bank_account:
    def __init__(self,name, balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            print("Insufficient balance")
    def display_balance(self):
        print(f"Account balance for {self.name}: ${self.balance}")
a=bank_account("John", 1000)
a.deposit(500)
a.withdraw(200)
a.display_balance()