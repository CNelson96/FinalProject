# I certify that the Python file I am submitting is all my own work.
# None of it is copied from any source or any person.
# Signed: Cory Nelson, Marcus Her, Nou Chai Thao.
# Date: 5/01/2026
#
# Author: Cory Nelson, Marcus Her, Nou Chai Thao.
# Date:  5/01/2026
# Class: CSS335
# Assignment: Final Project Banking
# File Name: Interpreter.py
# Description: Creating interpreter for DSL
#






from BankAccount import BankAccount

class Interpreter:
    def __init__(self):
        # Dictionary to store all bank accounts
        self.customer_accts = {}

        # Current account
        self.current_acct_num = ""

        # Running flag
        self.running = True

        # Load default accounts
        self.create_hard_coded_accounts()


    # --- MAIN ------------------------------------------------------
    def interpret(self, ast):
        if ast.get_node_type() == "ERROR":
            print("Interpreter Error: ", ast.get_value())

        elif ast.get_node_type() == "PROGRAM":
            self.interpret_program(ast)

        else:
            print("Interpreter Error: Expected PROGRAM node.")


    # --- INTERPRET PROGRAM ----------------------------------------
    def interpret_program(self, program_node):
        children = program_node.get_children()

        for child in children:
            if self.running:
                self.interpret_node(child)


    # --- INTERPRET NODE -------------------------------------------
    def interpret_node(self, node):
        node_type = node.get_node_type()

        match node_type:
            case "ACCOUNT_NUMBER":
                self.set_current_account(node.get_value())

            case "DEPOSIT":
                self.interpret_deposit(node)

            case "WITHDRAWAL":
                self.interpret_withdrawal(node)

            case "CHECK_BALANCE":
                self.interpret_check_balance()

            case "CREATE_ACCOUNT":
                self.interpret_create_account(node)

            case "CHECK_OTHER_ACCOUNT":
                self.set_current_account(node.get_value())

            case "EXIT_PROGRAM":
                self.running = False
                print("Goodbye")

            case _:
                print("Interpreter Error: Unknown node type: ", node_type)


    # --- SET CURRENT ACCOUNT --------------------------------------
    def set_current_account(self, acct_num):
        if acct_num not in self.customer_accts:
            print("Account number does not exist: ", acct_num)

        else:
            self.current_acct_num = acct_num
            print(f"Current account: {acct_num}")


    # --- DEPOSIT ---------------------------------------------------
    def interpret_deposit(self, node):
        if self.current_acct_num == "":
            print("No account selected.")

        else:
            children = node.get_children()
            amount = children[0].get_value()

            account = self.customer_accts[self.current_acct_num]
            account.deposit(amount)


    # --- WITHDRAW --------------------------------------------------
    def interpret_withdrawal(self, node):
        if self.current_acct_num == "":
            print("No account selected.")

        else:
            children = node.get_children()
            amount = children[0].get_value()

            account = self.customer_accts[self.current_acct_num]
            account.withdrawal(amount)

    # --- CHECK BALANCE ---------------------------------------------
    def interpret_check_balance(self):
        if self.current_acct_num == "":
            print("No account selected.")

        else:
            account = self.customer_accts[self.current_acct_num]
            balance = account.get_balance()
            print(f"Your current balance is ${balance:.2f}")


    # --- CREATE ACCOUNT --------------------------------------------
    def interpret_create_account(self, node):

        children = node.get_children()
        first_name = children[0].get_value()
        last_name = children[1].get_value()
        acct_num = children[2].get_value()
        balance = children[3].get_value()

        if acct_num in self.customer_accts:
            print("This account number already exists:", acct_num)

        else:
            self.customer_accts[acct_num] = BankAccount(first_name, last_name, acct_num, balance)
            print("Account created successfully: ", acct_num)


    # --- DEFAULT ACCOUNTS ------------------------------------------
    def create_hard_coded_accounts(self):

        self.customer_accts["CN123456"] = BankAccount("Cory", "Nelson", "CN123456", 500)
        self.customer_accts["NT654321"] = BankAccount("Nouchai", "Thao", "NT654321", 1200)
        self.customer_accts["MH246810"] = BankAccount("Marcus", "Her", "MH246810", 875)
        self.customer_accts["BW135790"] = BankAccount("Brian", "Wilson", "BW135790", 640)
        self.customer_accts["DT112233"] = BankAccount("Dana", "Thomas", "DT112233", 1500)
        self.customer_accts["EK445566"] = BankAccount("Emily", "King", "EK445566", 920)
        self.customer_accts["FR778899"] = BankAccount("Frank", "Roberts", "FR778899", 300)
        self.customer_accts["GH990011"] = BankAccount("Grace", "Hill", "GH990011", 2100)
        self.customer_accts["IJ223344"] = BankAccount("Isaac", "Johnson", "IJ223344", 760)
        self.customer_accts["KL556677"] = BankAccount("Karen", "Lewis", "KL556677", 1340)

