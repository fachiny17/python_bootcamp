class BankAccount:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        
    balance = 0
        
    def __str__(self):
        return f"Owner: {self.owner}, Account number: {self.account_number}, Account Balance: {self.balance}"
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance is ${self.balance}")
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount