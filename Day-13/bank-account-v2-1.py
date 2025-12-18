# Basic Bank Account System Version 2.1
# list that stores deposit/withdraw messages and prints out Transaction History with dates
# Implementing p7
# Python Dates
# [Dates](https://www.w3schools.com/python/python_datetime.asp)

from datetime import datetime


def show_menu():
    print("Welcome to the Bank Account System")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("5. View Transaction History")


def check_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")


def gettime():
    return datetime.now().strftime("%b %d, %Y %H:%M:%S")


def deposit(balance, history):
    amount = float(input("Enter amount to deposit: $"))
    if amount <= 0:
        print("Deposit amount must be more than $0.")
        return balance
    balance += amount
    message = f"{gettime()} | Credit |  ${amount:.2f} |  Balance | ${balance:.2f}"
    print(message)

    # Save to List
    history.append(message)
    # database code but later
    return balance


def withdraw(balance, history):
    amount = float(input("Enter amount to withdraw: $"))
    if amount <= 0:
        print("Withdrawal amount must be more than $0.")
        return balance
    if amount > balance:
        print("Insufficient funds!")
        history.append(f"Failed withdrawal of ${amount:.2f} (Insufficient funds)")
    else:
        # balance = balance +  amount
        balance -= amount  # same as above line
        message = f"{gettime()} | Debit |  ${amount:.2f} |  Balance | ${balance:.2f}"
        history.append(message)

    return balance


def print_transaction_history(history):
    if not history:
        print("No transactions yet.")
    else:
        print("Transaction History:")
        for item in history:
            print(" --- " + item)


def main():
    balance = 100.0  # Initial balance
    history = []  # List to store transaction history

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            balance = deposit(balance, history)
        elif choice == "2":
            balance = withdraw(balance, history)
        elif choice == "3":
            check_balance(balance)
        elif choice == "4":
            print("Thank you for using the Bank Account System. Goodbye!")
            break
        elif choice == "5":
            print_transaction_history(history)
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
