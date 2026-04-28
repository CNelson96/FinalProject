from BankAccount import BankAccount
import unittest


RUN_ALL_TESTS = 1
RUN_SPECIFIC_TEST = 2
SHOW_ALL_TESTS = 3
EXIT = 4


def main():


    user_input = 0

    while user_input != EXIT:

        user_input = display_test_options()

        if user_input == RUN_ALL_TESTS:
            print("====Running All Tests====")
            run_all_tests()

        elif user_input == RUN_SPECIFIC_TEST
            print("Choose a specific test to run")

        elif user_input == SHOW_ALL_TESTS:
            print("Test balance after withdrawal")
            print("Test balance after deposit")
            print("Test account number created")
            print("Test first name exists")
            print("Test last name exists")
            print("Test balance exists")


        elif user_input == EXIT:
            print("====Leaving Testing Environment====")

        else:
            print("Invalid option")



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

def run_all_tests():
    testing_suite = unittest.TestLoader().loadTestsFromTestCase(TestBankAccount)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(testing_suite)


class TestBankAccount(unittest.TestCase):


    def test_balance_after_withdrawal(self):
        acct = BankAccount("Cory", "Nelson", "CN856235", 800)
        actual_value = acct.withdrawal(50)
        expected_outcome = 750

        if actual == expected_outcome:
            print("PASS")
        else:
            print("FAIL")

        self.assertEqual(expected_outcome, actual_value)



    def test_balance_after_deposit(self):
        acct = BankAccount("Cory", "Nelson", "CN856235", 800)
        actual_value = acct.deposit(50)
        expected_outcome = 850

        if actual == expected_outcome:
            print("PASS")
        else:
            print("FAIL")

        self.assertEqual(expected_outcome,actual_value)


    def test_account_number_created(self):
        acct = BankAccount("Cory", "Nelson", "CN856235", 800)
        actual_value = acct.get_acct_num()
        expected_outcome = "CN856235"


        if actual == expected_outcome:
            print("PASS: ")
        else:
            print("FAIL: ")

        self.assertEqual(expected_outcome, actual_value)


    def test_first_name_exists(self):
        acct = BankAccount("Cory", "Nelson", "CN856235", 800)
        actual_value = acct.get_acct_first_name()
        expected_outcome = "Cory"

        if actual_value == expected_outcome:
            print("PASS")
        else:
            print("FAIL")

        self.assertEqual(expected_outcome, actual_value)

    def test_last_name_exists(self):
        acct = BankAccount("Cory", "Nelson", "CN856235", 800)
        actual_value = acct.get_acct_last_name()
        expected_outcome = "Nelson"

        if actual value == expected_outcome:
            print("PASS")
        else:
            print("FAIL")


    def test_balance_exists(self):
        acct = BankAccount("Cory", "Nelson", "CN856235", 800)
        actual_value = acct.get_acct_balance()
        expected_outcome = 800

        if actual_value == expected_outcome:
            print("PASS")
        else:
            print("FAIL")



            








if __name__ == "__main__":
    main()
