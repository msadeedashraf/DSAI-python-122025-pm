# account number = 123456
# account holder name = John Doe
# balance = 1000

# create a bank account class with properties and methods to deposit, withdraw and check balance

# Implementing additional features like automatic account number generation (IBAN), account creation date, and account activation status


from datetime import datetime


class BankAccount:
    def __init__(self, account_holder_name, balance=0):
        self.account_number = self.generate_iban()
        self.account_holder_name = account_holder_name
        self.balance = balance
        self.creation_date = datetime.now()
        self.is_active = False

    def deposit(self, amount):

        if not self.is_active:
            print(
                f"Account is not active. {amount} can't be deposited. Please activate your account to proceed."
            )
            return

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
        print(
            f"Account Creation Date: {self.creation_date.strftime('%Y-%m-%d %H:%M:%S')}"
        )
        print(f"Account Active: {self.is_active}")

    # creating a method to generate a account number automatically - IBAN
    def generate_iban(self):
        import random

        country_code = "GB"
        check_digits = str(random.randint(10, 99))
        bank_identifier = "BANK"
        account_number = str(random.randint(10000000, 99999999))
        iban = f"{country_code}{check_digits}{bank_identifier}{account_number}"
        return iban

    def activate_account(self):
        self.is_active = True
        print(f"Account {self.account_number} activated.")


# Example usage

print("--------------------")

account1 = BankAccount("Sandy")
account1.activate_account()
account1.deposit(5000)
account1.account_info()

print("--------------------")

account2 = BankAccount("UV")
account2.account_info()

print("--------------------")

account3 = BankAccount("Asim")
account3.account_info()

# Don't Repeat Yourself ----- DRY
