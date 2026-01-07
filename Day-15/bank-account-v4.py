# Safer Input + Daily Withdrawal Limit + Better Functions

# get_positive_amount() → keeps asking until user enters a valid number

# get_menu_choice() → validates menu input

# Simple “daily withdrawal limit” to show more logic

# Same PIN + history + ATM structure


def show_menu():
    print("\n=== ATM MENU (SAFE VERSION) ===")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transaction History")
    print("5. Exit")


def get_positive_amount(prompt):
    """
    Asks the user for a positive number.
    Keeps asking until a valid number > 0 is entered.
    Returns a float.
    """
    while True:
        user_input = input(prompt)
        try:
            amount = float(user_input)
            if amount <= 0:
                print("Amount must be greater than 0. Try again.")
            else:
                return amount
        except ValueError:
            print("Please enter a valid number (e.g. 100 or 99.50).")


def get_menu_choice():
    """
    Asks the user for a menu choice between 1 and 5.
    Keeps asking until a valid choice is entered.
    """
    while True:
        choice = input("Choose an option (1–5): ").strip()
        if choice in ["1", "2", "3", "4", "5"]:
            return choice
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


def check_balance(balance):
    print(f"\nYour current balance is: ${balance:.2f}")


def deposit(balance, history):
    amount = get_positive_amount("Enter amount to deposit: $")
    balance += amount
    message = f"Deposited ${amount:.2f}. New balance: ${balance:.2f}"
    print(message)
    history.append(message)
    return balance


def withdraw(balance, history, daily_limit, withdrawn_today):
    """
    Withdraw money with:
    - Positive amount check
    - Sufficient balance check
    - Daily limit check
    Returns updated (balance, withdrawn_today)
    """
    amount = get_positive_amount("Enter amount to withdraw: $")

    # Check daily limit
    if withdrawn_today + amount > daily_limit:
        message = (
            f"Withdrawal of ${amount:.2f} denied. "
            f"Daily limit of ${daily_limit:.2f} would be exceeded."
        )
        print(message)
        history.append(message)
        return balance, withdrawn_today

    # Check balance
    if amount > balance:
        message = f"Failed withdrawal of ${amount:.2f} (Insufficient funds)."
        print("Insufficient funds.")
        history.append(message)
        return balance, withdrawn_today

    # Success
    balance -= amount
    withdrawn_today += amount
    message = (
        f"Withdrew ${amount:.2f}. New balance: ${balance:.2f}. "
        f"Withdrawn today: ${withdrawn_today:.2f}/{daily_limit:.2f}"
    )
    print(message)
    history.append(message)
    return balance, withdrawn_today


def print_history(history):
    print("\n=== TRANSACTION HISTORY ===")
    if len(history) == 0:
        print("No transactions yet.")
    else:
        for item in history:
            print("- " + item)


def pin_check(correct_pin, max_attempts=3):
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

    # Simple daily withdrawal limit
    daily_limit = 500.00
    withdrawn_today = 0.00

    print("Welcome to Python Bank ATM (Safe Version)!")

    # PIN verification
    if not pin_check(pin):
        return

    # Main ATM loop
    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit(balance, history)
        elif choice == "3":
            balance, withdrawn_today = withdraw(
                balance, history, daily_limit, withdrawn_today
            )
        elif choice == "4":
            print_history(history)
        elif choice == "5":
            print("Thank you for using Python Bank ATM. Goodbye!")
            break


if __name__ == "__main__":
    main()
