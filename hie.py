class BankAccount:
    def __init__(self, account_holder, balance):   
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Current balance: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Current balance: {self.balance}")
    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):    
        super().__init__(account_holder, balance)                 
        self.interest_rate = interest_rate
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: {interest}. Current balance: {self.balance}")
class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):    
        super().__init__(account_holder, balance)                    
        self.overdraft_limit = overdraft_limit

    def withdraw_with_overdraft(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Transaction exceeds overdraft limit!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Current balance: {self.balance}")
print("Savings Account:")
savings_account = SavingsAccount("John Doe", 50000, 0.05)
savings_account.display_balance()
savings_account.deposit(20000)
savings_account.add_interest()
savings_account.withdraw(10000)
savings_account.display_balance()
print("\nCurrent Account:")
current_account = CurrentAccount("Jane Doe", 30000, 20000)
current_account.display_balance()
current_account.deposit(15000)
current_account.withdraw_with_overdraft(40000)
current_account.display_balance()
