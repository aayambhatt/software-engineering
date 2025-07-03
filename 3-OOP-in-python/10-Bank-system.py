class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Rs {amount} deposited in your bank account")
        else:
            raise Exception("Cannot deposit negative amount")
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception("Not Enough balance")
        else:
            self.balance -= amount
            print(f"Withdrew Rs {amount}")

    def check_balance(self):
        print(f"Balance is: {self.balance}")

user1 = Account("Aayam", 500)
user1.check_balance()
user1.deposit(500)
user1.check_balance()
user1.withdraw(1050)