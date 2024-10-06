class BankAccount:
    def __init__(self, initial_balance=0): #initialize an account_balance attribute with optional starting balalnce defaulting to zero
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return "Deposited"
        else:
            print("Deposit amount must be above zero")

    def withdraw(self, amount):
        if amount > self.account_balance:
            return False
        else:
            self.account_balance -= amount
            return True
        
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")  