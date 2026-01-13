# Inheritance and Advanced OOP Concepts in Bank Account Management

# Extending the BankAccount class to create SavingsAccount and CurrentAccount with specific features

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


class SavingsAccount(BankAccount):
    def __init__(self, account_holder_name, balance=0, interest_rate=0.02):
        # Call the constructor of the parent class
        super().__init__(account_holder_name, balance)
        self.interest_rate = interest_rate

    def add_intrest(self):
        if not self.is_active:
            print(
                "Account is not active. Interest can't be added. Please activate your account to proceed."
            )
            return

        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: {interest}. New balance: {self.balance:.2f}")


class CurrentAccount(BankAccount):
    def __init__(self, account_holder_name, balance=0, overdraft_limit=500):
        # Call the constructor of the parent class
        super().__init__(account_holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if not self.is_active:
            print(
                f"Account is not active. {amount} can't be withdrawn. Please activate your account to proceed."
            )
            return
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        # CurrentAccount allows overdraft up to the overdraft_limit
        if self.balance - amount < -self.overdraft_limit:
            print("Withdrawal exceeds overdraft limit. Cannot withdraw.")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")


# Example usage
print("=== Savings Account ===")
s1 = SavingsAccount("Alice", 1000, 0.03)
s1.activate_account()
s1.account_info()
s1.add_intrest()

print("\n after adding interest:")
s1.account_info()


print("\n=== Current Account ===")

c1 = CurrentAccount("Bob", 500, 300)
c1.activate_account()
c1.withdraw(700)  # Within overdraft limit
c1.account_info()

print("\n  withdrawal exceeding the overdraft limit:")

c1.withdraw(200)  # Exceeds overdraft limit
c1.account_info()

print("\n withdrawal under the overdraft limit:")
c1.withdraw(100)  # Valid withdrawal
c1.account_info()
