class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
                
    def __str__(self):
        return f"Owner: {self.owner}, Account number: {self.account_number}, Account Balance: {self.balance}"
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance is ${self.balance}")
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Debit alert! \nDear {self.owner}, you have successfully withdrawn ${amount}. New balance is ${self.balance}. \nThanks for banking with us.")
        else:
            print(f"Insufficient balance! \nYou cannot withdraw ${amount} because your balance is only {self.balance}.")
        
    def check_balance(self):
        print(f"Account balance: ${self.balance}")
        

account = BankAccount("01234567", "Chisom")
while True:
    print("\nBank Account Menu")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balanace")    
    print("4. Exit")
    
    choice = input("Enter your choice from the above options: ")
    
    if choice in ["1","Deposit"]:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    
    elif choice in ["2","Withdraw"]:
        amount = float(input("Enter the amount to withdraw: "))
        account.withdraw(amount)
        
    elif choice in ["3","Check Balance"]:
        account.check_balance()
        
    elif choice in ["4","Exit"]:
        print("Exiting the Bank Account Management System. Thanks for banking with us!")
        break
    
    else:
        print("Invalid choice. Please choose from the options provided above.")