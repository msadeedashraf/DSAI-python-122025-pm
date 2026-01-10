# account number = 123456
# account holder name = John Doe
# balance = 1000

# create a bank account class with properties and methods to deposit, withdraw and check balance


class BankAccount:
    def __init__(self, account_number, account_holder_name, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: {amount}. New balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder Name: {self.account_holder_name}")
        print(f"Balance: {self.balance}")


# Example usage

print("--------------------")

account1 = BankAccount(123456, "John Doe", 1000)
account1.account_info()


print("--------------------")
account2 = BankAccount(7686786786786, "Sadeed", 10000)
account2.deposit(5000)
account2.account_info()

print("--------------------")

account3 = BankAccount(9898998989, "Kris", 20000)
account3.account_info()
