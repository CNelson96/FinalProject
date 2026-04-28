from BankAccount import BankAccount

# Global Constants
MAKE_DEPOSIT = 1
MAKE_WITHDRAWAL = 2
CHECK_BALANCE = 3
CREATE_ACCT = 4
CHECK_OTHER_ACCT = 5
EXIT = 6


# Main function that runs the banking menu system
def main():


    user_input = 0
    customer_accts = {}

    #Loading starter accounts
    create_hard_coded_accounts(customer_accts)

    print("\nWelcome to the banking program (Type EXIT at anytime to leave the program)")
    print()

    # Ask user for account number
    acct_num = input("Enter account number: ").upper()

    # Allow exit before loop begins
    if acct_num == "EXIT":
        user_input = EXIT
        print("Goodbye")

    # Main program loop
    while user_input != EXIT:

        # If account exists, allow access
        if acct_num in customer_accts:

            # Show menu options
            user_input = display_options()

            # Deposit money
            if user_input == MAKE_DEPOSIT:
                amount = input("Enter a deposit amount: ").upper()

                if amount == "EXIT":
                    user_input = EXIT

                else:

                    try:
                        amount = float(amount)
                        customer_accts[acct_num].deposit(amount)
                    except ValueError:
                        print("Deposit must be a valid number")


            # Withdraw money
            elif user_input == MAKE_WITHDRAWAL:
                amount = input("Enter a withdrawal amount: ").upper()

                if amount == "EXIT":
                    user_input = EXIT

                else:
                    try:
                        amount = float(amount)
                        customer_accts[acct_num].withdrawal(amount)
                    except ValueError:
                        print("Withdrawal must be a valid number")

            # Show balance
            elif user_input == CHECK_BALANCE:
                print("\nYour current balance is $" + f"{customer_accts[acct_num].get_balance():.2f}")

            # Create new account
            elif user_input == CREATE_ACCT:
                result = create_account(customer_accts)

                if result == EXIT:
                    user_input = EXIT
                    print("Goodbye")

            # Switch to another account
            elif user_input == CHECK_OTHER_ACCT:
                acct_num =  input("Enter account number: ").upper()

                if acct_num == "EXIT":
                    user_input = EXIT
                    print("Goodbye")

            # Exit program
            elif user_input == EXIT:
                print("Goodbye")

        # Invalid account number entered
        else:
            print("Account number doesn't exist")
            acct_num = input("Enter account number: ").upper()

            if acct_num == "EXIT":
                user_input = EXIT
                print("Goodbye")

# Displays menu options and validates user selection
def display_options():
        print('\n1. Make a deposit')
        print("2. Make a withdrawal")
        print("3. Check the balance")
        print("4. Create Account")
        print("5. Check another Account")
        print("6. Exit")

        choice = input("Choose an option: ").upper()

        # Validate menu choice
        while  choice != "EXIT" and (not choice.isdigit() or int(choice) < 1 or int(choice) > 6):
            print("Invalid selection. Please choose a number (1-6).")
            choice = input("Choose an option: ").upper()

        result = EXIT

        if choice != "EXIT":
            result = int(choice)

        return result



# Creates a brand new account
def create_account(customer_accts):

    result = 0

    #Get first name
    first_name = input("First name: ").upper()

    if first_name == "EXIT":
        result = EXIT

    # Validate first name
    if result != EXIT:
        while first_name.isalpha() == False:
            print("First name must contain letters only.")
            first_name = input("First name: ").upper()

            if first_name == "EXIT":
                result = EXIT

    # Get last name
    if result != EXIT:
        last_name = input("Last name: ").upper()

        if last_name == "EXIT":
            result = EXIT

    # Validate last name
    if result != EXIT:
        while last_name.isalpha() == False:
            print("Last name must contain letters only.")
            last_name = input("Last name: ").upper()

            if last_name == "EXIT":
                result = EXIT

    # Get account number
    if result != EXIT:
        acct_num = input("Enter an account name (Account name must start "
                         "with first and last initial followed by 6 numbers) ").upper()

        if acct_num == "EXIT":
            result = EXIT

    # Prevent duplicate account numbers
    if result != EXIT:
        while acct_num in customer_accts and acct_num != "EXIT":
            print("This account number already exists, choose a different one")
            acct_num = input("Enter an account name (Account name must start "
                             "with first and last initial followed by 6 numbers) ").upper()

            if acct_num == "EXIT":
                result = EXIT

    # Get starting balance
    if result != EXIT:
        balance = input("Starting balance: ").upper()

        while balance != "EXIT":
            try:
                balance = float(balance)
                customer_accts[acct_num] = BankAccount(first_name, last_name, acct_num, balance)
                print("Account created successfully.")
                balance = "EXIT"

            except ValueError:
                print("Starting balance must be a valid number.")
                balance = input("Starting balance: ").upper()

        if balance == "EXIT" and acct_num not in customer_accts:
            result = EXIT

    return result


# Creates starter accounts for testing
def create_hard_coded_accounts(customer_accts):
    customer_accts["CN123456"] = BankAccount("Cory", "Nelson", "CN123456", 500)
    customer_accts["NT654321"] = BankAccount("Nouchai", "Thao", "NT654321", 1200)
    customer_accts["MH246810"] = BankAccount("Marcus", "Her", "MH246810", 875)
    customer_accts["BW135790"] = BankAccount("Brian", "Wilson", "BW135790", 640)
    customer_accts["DT112233"] = BankAccount("Dana", "Thomas", "DT112233", 1500)
    customer_accts["EK445566"] = BankAccount("Emily", "King", "EK445566", 920)
    customer_accts["FR778899"] = BankAccount("Frank", "Roberts", "FR778899", 300)
    customer_accts["GH990011"] = BankAccount("Grace", "Hill", "GH990011", 2100)
    customer_accts["IJ223344"] = BankAccount("Isaac", "Johnson", "IJ223344", 760)
    customer_accts["KL556677"] = BankAccount("Karen", "Lewis", "KL556677", 1340)



if __name__ == "__main__":
    main()
