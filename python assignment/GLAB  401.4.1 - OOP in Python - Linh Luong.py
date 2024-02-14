# task 5
'''
In this example, we assume a simplified banking system with classes for Bank, Account, and Customer. The Bank class manages multiple accounts and can generate account statements. The Account class represents a customer account and can perform deposit and withdrawal operations. The Customer class holds the customer's information.

TO DOs - 1
You should modify the code according to the specific requirements of the banking system. Use these instructions to integrate changes in the provided code snippet: 
Add Account Validation:
Create a method in the Bank class to check if an account with a specific account number already exists before creating a new account. Print a message if the account already exists.

Display Initial Deposit Message:
Modify the deposit method in the Account class to print a message indicating the successful deposit.

Minimum Withdrawal Amount:
Set a minimum withdrawal amount in the withdrawal method of the Account class. If the withdrawal amount is below this minimum, print a message indicating the minimum withdrawal requirement.

'''
class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []
        
    def check_account(self, account): # method to check if specific account number already exist
        for i in range(len(self.accounts)):
            if account.account_number == self.accounts[i].account_number:   
                print("Account already existed.")
                return True
            else:
                print("Account not exist.")
                return False
                
    def create_account(self, account):
            self.accounts.append(account)

    def generate_account_statements(self):
        for account in self.accounts:
            print(f"Account Number: {account.account_number}")
            print(f"Customer Name: {account.customer.name}")
            print(f"Balance: {account.balance}")
            
 
class Customer:
    def __init__(self, name):
        self.name = name

class Account:
    def __init__(self, account_number, customer):
        self.account_number = account_number
        self.customer = customer
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Deposit success") # method to print out successful deposit

    def withdraw(self, amount):
        if self.balance >= amount:
            if amount < 100: # Method to check for minimum withraw
                print("Can't withdraw. Minimum withraw amount is 100.")
            else:
                self.balance -= amount
        else:
            print("Insufficient balance")

# Create objects and perform banking operations
customer1 = Customer("John Doe")
account1 = Account(12345, customer1)
account1.deposit(1000)
account1.withdraw(50)
account1.withdraw(500)

customer2 = Customer("Jane Smith")
account2 = Account(54321, customer2)
account2.deposit(2000)

bank = Bank("MyBank")
if not bank.check_account(account1):
    bank.create_account(account1)
if not bank.check_account(account2):
    bank.create_account(account2)


customer3 = Customer("Linh Luong")
account3 = Account(12345, customer3)
bank.check_account(account3)

bank.generate_account_statements()