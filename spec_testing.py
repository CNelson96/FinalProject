# I certify that the Python file I am submitting is all my own work.
# None of it is copied from any source or any person.
# Signed: Cory Nelson, Marcus Her, Nou Chai Thao.
# Date: 5/01/2026
#
# Author: Cory Nelson, Marcus Her, Nou Chai Thao.
# Date:  5/01/2026
# Class: CSS335
# Assignment: Final Project Banking
# File Name: spec_testing.py
# Description: Specification testing to test functions
#







#Importing BankAccount class from BankAccount file
from BankAccount import BankAccount

#Importing Python unit testing
import unittest


#Menu globals
RUN_ALL_TESTS = 1
RUN_SPECIFIC_TEST = 2
SHOW_ALL_TESTS = 3
EXIT = 4


def main():
    user_input = 0

    # continue running unless user selects exit
    while user_input != EXIT:

        user_input = display_test_options()

        # run all tests
        if user_input == RUN_ALL_TESTS:
            print("====Running All Tests====")
            run_all_tests()

        # choosing a selected test
        elif user_input == RUN_SPECIFIC_TEST:
            show_test_options()
            choice = input("Enter the number of the test you would like to run: ")


            # validating choice
            while choice != "EXIT" and (not choice.isdigit() or int(choice) < 1 or int(choice) > 12):
                print("Invalid selection. Please choose a number (1-12).")
                choice = input("Choose an option: ").upper()

            if choice != "EXIT":
                run_specific_test(choice)

        #show a list of all tests
        elif user_input == SHOW_ALL_TESTS:
            show_test_options()

        # Exiting program
        elif user_input == EXIT:
            print("====Leaving Testing Environment====")

        else:
            print("Invalid option")

#Function of menu options
def display_test_options():
    print('\n1. Run all tests')
    print("2. Run a specific test")
    print("3. Show all tests")
    print("4. Exit")

    choice = input("Choose an option: ").upper()

    # Validate menu choice
    while choice != "EXIT" and (not choice.isdigit() or int(choice) < 1 or int(choice) > 4):
        print("Invalid selection. Please choose a number (1-4).")
        choice = input("Choose an option: ").upper()

    result = EXIT

    if choice != "EXIT":
        result = int(choice)

    return result

#Function that shows all test options
def show_test_options():
    print("1. Test balance after withdrawal")
    print("2. Test balance after deposit")
    print("3. Test account number created")
    print("4. Test first name exists")
    print("5. Test last name exists")
    print("6. Test balance exists")
    print("7. Test negative withdrawal amount")
    print("8. Test negative deposit amount")
    print("9. Test withdrawal over balance")
    print("10. Test withdrawal of zero")
    print("11. Test deposit of zero")
    print("12. Test multiple transactions")



#Function that uses unittest to run all tests
def run_all_tests():
    testing_suite = unittest.TestLoader().loadTestsFromTestCase(TestBankAccount)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(testing_suite)

#Function that runs a selected test
def run_specific_test(test_to_run):
    tests = {
        "1": "test_balance_after_withdrawal",
        "2": "test_balance_after_deposit",
        "3": "test_account_number_created",
        "4": "test_first_name_exists",
        "5": "test_last_name_exists",
        "6": "test_balance_exists",
        "7": "test_negative_withdrawal_amount",
        "8": "test_negative_deposit_amount",
        "9": "test_amount_withdrawal_over_balance",
        "10": "test_withdrawal_of_zero",
        "11": "test_deposit_of_zero",
        "12": "test_multiple_transactions"
    }

    #Creating a test suite with only one selected test
    testing_suite = unittest.TestSuite()
    testing_suite.addTest(TestBankAccount(tests[test_to_run]))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(testing_suite)

#Unit testing class
class TestBankAccount(unittest.TestCase):

    #Test withdrawal lowers balance correctly
    def test_balance_after_withdrawal(self):

        print("Testing balance after withdrawal")
        acct = BankAccount("Cory", "Nelson", "CN856235", 800)
        actual_value = acct.withdrawal(50)
        expected_outcome = 750

        if actual_value == expected_outcome:
            print(f"PASS: Test_balance_after_withdrawal returned {actual_value} which matched the expected outcome of {expected_outcome}")
        else:
            print(f"FAIL: Test_balance_after_withdrawal returned {actual_value} which does not match the expected outcome of {expected_outcome}")

        self.assertEqual(expected_outcome, actual_value)

    # Test deposit increases balance correctly
    def test_balance_after_deposit(self):
        print("Testing balance after deposit")
        acct = BankAccount("Cory", "Nelson", "CN856235", 800)
        actual_value = acct.deposit(50)
        expected_outcome = 850

        if actual_value == expected_outcome:
            print(f"PASS: test_balance_after_deposit returned {actual_value} which matched the expected outcome of {expected_outcome}")
        else:
            print(f"FAIL: test_balance_after_deposit returned {actual_value} which does not match the expected outcome of {expected_outcome}")

        self.assertEqual(expected_outcome, actual_value)

    # Test account number getter
    def test_account_number_created(self):
        print("Testing account number created")
        acct = BankAccount("Cory", "Nelson", "CN856235", 800)
        actual_value = acct.get_acct_num()
        expected_outcome = "CN856235"

        if actual_value == expected_outcome:
            print("PASS:  test_account_number_created returned " + actual_value + " which matched the expected outcome of" + expected_outcome)
        else:
            print("FAIL:  test_account_number_created returned " + actual_value + " which does not match the expected outcome of" + expected_outcome)

        self.assertEqual(expected_outcome, actual_value)

    # Test first name getter
    def test_first_name_exists(self):
        print("Testing first name exists")
        acct = BankAccount("Cory", "Nelson", "CN856235", 800)
        actual_value = acct.get_first_name()
        expected_outcome = "Cory"

        if actual_value == expected_outcome:
            print("PASS: test_first_name_exists returned " + actual_value + " which matched the expected outcome of" + expected_outcome)
        else:
            print("FAIL: test_first_name_exists returned " + actual_value + " which does not match the expected outcome of" + expected_outcome)

        self.assertEqual(expected_outcome, actual_value)

    # Test last name getter
    def test_last_name_exists(self):
        print("Testing last name exists")
        acct = BankAccount("Cory", "Nelson", "CN856235", 800)
        actual_value = acct.get_last_name()
        expected_outcome = "Nelson"

        if actual_value == expected_outcome:
            print("PASS: test_last_name_exists returned " + actual_value + "which matched the expected outcome of" + expected_outcome)
        else:
            print("FAIL: test_last_name_exists returned " + actual_value + "which does not match the expected outcome of" + expected_outcome)

        self.assertEqual(expected_outcome, actual_value)

    # Test starting balance getter
    def test_balance_exists(self):
        print("Testing balance exists")
        acct = BankAccount("Cory", "Nelson", "CN856235", 800)
        actual_value = acct.get_balance()
        expected_outcome = 800

        if actual_value == expected_outcome:
            print(f"PASS: test_balance_exists returned {actual_value} which matched the expected outcome of {expected_outcome}")
        else:
            print(f"FAIL: test_balance_exists returned {actual_value} which does not match the expected outcome of {expected_outcome}")

        self.assertEqual(expected_outcome,actual_value)

    # Test negative withdrawal does nothing
    def test_negative_withdrawal_amount(self):
        print("Testing negative withdrawal amount")
        acct = BankAccount("Cory", "Nelson", "CN856235", 800)
        actual_value = acct.withdrawal(-1000)
        expected_outcome = 800

        if actual_value == expected_outcome:
            print(f"PASS: test_negative_withdrawal_amount returned {actual_value} which matched the expected outcome of {expected_outcome}")
        else:
            print(f"FAIL: test_negative_withdrawal_amount returned {actual_value} which does not match the expected outcome of {expected_outcome}")

        self.assertEqual(expected_outcome, actual_value)

    # Test negative deposit does nothing
    def test_negative_deposit_amount(self):
        print("Testing negative deposit")
        acct = BankAccount("Cory", "Nelson", "CN856235", 800)
        actual_value = acct.deposit(-1000)
        expected_outcome = 800

        if actual_value == expected_outcome:
            print(f"PASS: test_negative_deposit_amount returned {actual_value} which matched the expected outcome of {expected_outcome}")
        else:
            print(f"FAIL: test_negative_deposit_amount returned {actual_value} which does not match the expected outcome of {expected_outcome}")

        self.assertEqual(expected_outcome, actual_value)

    # Test withdrawing more than balance fails
    def test_amount_withdrawal_over_balance(self):
        print("Testing amount of withdrawal over balance amount")
        acct = BankAccount("Cory", "Nelson", "CN856235", 800)
        actual_value = acct.withdrawal(1000)
        expected_outcome = 800

        if actual_value == expected_outcome:
            print(f"PASS: test_amount_withdrawal_over_balance returned {actual_value} which matched the expected outcome of {expected_outcome}")
        else:
            print(f"FAIL: test_amount_withdrawal_over_balance returned {actual_value} which does not match the expected outcome of {expected_outcome}")

        self.assertEqual(expected_outcome, actual_value)

    # Test withdrawing zero does nothing
    def test_withdrawal_of_zero(self):
        print("Testing a withdrawal of 0")
        acct = BankAccount("Cory", "Nelson", "CN856235", 800)
        actual_value = acct.withdrawal(0)
        expected_outcome = 800

        if actual_value == expected_outcome:
            print(f"PASS: test_withdrawal_of_zero returned {actual_value} which matched the expected outcome of {expected_outcome}")
        else:
            print(f"FAIL: test_withdrawal_of_zero returned {actual_value} which does not match the expected outcome of {expected_outcome}")

        self.assertEqual(expected_outcome, actual_value)

    # Test depositing zero does nothing
    def test_deposit_of_zero(self):
        print("Testing a deposit of 0")
        acct = BankAccount("Cory", "Nelson", "CN856235", 800)
        actual_value = acct.deposit(0)
        expected_outcome = 800

        if actual_value == expected_outcome:
            print(f"PASS: test_deposit_of_zero returned {actual_value} which matched the expected outcome of {expected_outcome}")
        else:
            print(f"FAIL: test_deposit_of_zero returned {actual_value} which does not match the expected outcome of {expected_outcome}")

        self.assertEqual(expected_outcome, actual_value)

    # Test multiple transactions in sequence
    def test_multiple_transactions(self):
        print("Testing multiple transactions")
        acct = BankAccount("Cory", "Nelson", "CN856235", 800)
        acct.deposit(200)
        actual_value = acct.withdrawal(600)
        expected_outcome = 400

        if actual_value == expected_outcome:
            print(f"PASS: test_multiple_transactions returned {actual_value} which matched the expected outcome of {expected_outcome}")
        else:
            print(f"FAIL: test_multiple_transactions returned {actual_value} which does not match the expected outcome of {expected_outcome}")

        self.assertEqual(expected_outcome, actual_value)




if __name__ == "__main__":
    main()
