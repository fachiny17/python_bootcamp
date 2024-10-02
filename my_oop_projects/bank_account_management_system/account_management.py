class BankAccount:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        
    balance = 0
        
    def __str__(self):
        return f"Owner: {self.owner}, Account number: {self.account_number}, Account Balance: {self.balance}"
    
    def deposit(self, amount):
        amount = input("Enter the amount you want to deposit: ")
        self.balance += amount
        print(f"Deposited ${amount}. New balance is ${self.balance}")
        
    def withdraw(self, amount):
        amount = input("Entr the amount you want to withdraw: ")
        if amount <= self.balance:
            self.balance -= amount
            print(f"Debit alert! \nDear {self.owner}, you have successfully withdrawn ${amount}. New balance is ${self.balance}. \nThanks for banking with us.")
        else:
            print(f"Insufficient balance! \nYou cannot withdraw ${amount} because your balance is only {self.balance}.")
        
    def check_balance(self):
        print(f"Account balance: ${self.balance}")
        

account = BankAccount()
while True:
    print("\nBank Account Menu")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balanace")    
    