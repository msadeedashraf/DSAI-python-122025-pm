# Basic Bank Account System Version 3.0
# Add PIN + ATM Simulation
# list that stores deposit/withdraw messages and prints out Transaction History

# PIN check (pin_check() function, 3 attempts)

# “ATM style” flow: you must pass PIN to access the menu


def show_menu():
    print("\n=== ATM MENU ===")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transaction History")
    print("5. Exit")


def check_balance(balance):
    print(f"\nYour current balance is: ${balance:.2f}")


def deposit(balance, history):
    amount = float(input("Enter amount to deposit: $"))
    if amount <= 0:
        print("Deposit must be more than $0.")
        return balance

    balance += amount
    message = f"Deposited ${amount:.2f}. New balance: ${balance:.2f}"
    print(message)
    history.append(message)
    return balance


def withdraw(balance, history):
    amount = float(input("Enter amount to withdraw: $"))
    if amount <= 0:
        print("Withdrawal must be more than $0.")
        return balance

    if amount > balance:
        print("Insufficient funds.")
        history.append(f"Failed withdrawal of ${amount:.2f} (Insufficient funds)")
        return balance

    balance -= amount
    message = f"Withdrew ${amount:.2f}. New balance: ${balance:.2f}"
    print(message)
    history.append(message)
    return balance


def print_history(history):
    print("\n=== TRANSACTION HISTORY ===")
    if len(history) == 0:
        print("No transactions yet.")
    else:
        for item in history:
            print("- " + item)


def pin_check(correct_pin, max_attempts=3):
    """
    Simple PIN check: user has max_attempts tries.
    Returns True if PIN is correct, False otherwise.
    """
    attempts = 0
    while attempts < max_attempts:
        entered_pin = input("Enter your 4-digit PIN: ")
        if entered_pin == correct_pin:
            print("PIN accepted.\n")
            return True
        else:
            attempts += 1
            print(f"Incorrect PIN. Attempts left: {max_attempts - attempts}")

    print("Too many incorrect attempts. Card blocked (simulation).")
    return False


def main():
    # Initial account state
    balance = 500.00
    history = []
    pin = "1234"

    print("Welcome to Python Bank ATM!")

    # Step 1: PIN verification
    if not pin_check(pin):
        # If PIN is wrong too many times, exit program
        return

    # Step 2: ATM main loop
    while True:
        show_menu()
        choice = input("Choose an option (1–5): ")

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit(balance, history)
        elif choice == "3":
            balance = withdraw(balance, history)
        elif choice == "4":
            print_history(history)
        elif choice == "5":
            print("Thank you for using Python Bank ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 5.")


if __name__ == "__main__":
    main()
