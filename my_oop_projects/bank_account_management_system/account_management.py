class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        
    def __str__(self):
        return f"Account number: {self.account_number}, Account Balance: {self.balance}"