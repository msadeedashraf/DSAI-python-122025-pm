# Basic Bank Account System Version 1.0
# No OOP, no ATM, no PIN system yet


def show_menu():
    print("Welcome to the Bank Account System")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")


def check_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")


def deposit(balance):
    amount = float(input("Enter amount to deposit: $"))
    if amount <= 0:
        print("Deposit amount must be more than $0.")
        return balance
    balance += amount
    print(f"Deposited: ${amount:.2f}. New balance: ${balance:.2f}")
    return balance


def withdraw(balance):
    amount = float(input("Enter amount to withdraw: $"))
    if amount <= 0:
        print("Withdrawal amount must be more than $0.")
        return balance
    if amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount
        print(f"Withdrew: ${amount:.2f}. New balance: ${balance:.2f}")
    return balance


def main():
    balance = 100.0  # Initial balance
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            balance = deposit(balance)
        elif choice == "2":
            balance = withdraw(balance)
        elif choice == "3":
            check_balance(balance)
        elif choice == "4":
            print("Thank you for using the Bank Account System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
