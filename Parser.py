# I certify that the Python file I am submitting is all my own work.
# None of it is copied from any source or any person.
# Signed: Cory Nelson, Marcus Her, Nou Chai Thao.
# Date: 5/01/2026
#
# Author: Cory Nelson, Marcus Her, Nou Chai Thao.
# Date:  5/01/2026
# Class: CSS335
# Assignment: Final Project Banking
# File Name: Parser.py
# Description: Creating the parser for the banking program
#




from Token import (TOKEN_ACCOUNT_NUMBER, TOKEN_MENU_CHOICE, TOKEN_AMOUNT,
                   TOKEN_NAME, TOKEN_EXIT, TOKEN_EOF)
from ASTNode import ASTNode

# Builds an AST from the token list produced by the Lexer.
# Each private method maps to one rule in the EBNF grammar.
# Returns an ERROR node if the input doesn't match the grammar.
class Parser:

    # Store the token list and set the starting position
    def __init__(self, tokens):
        self.__tokens = tokens
        self.__pos    = 0

    # Entry point: starts the parse and prints the resulting AST
    def parse(self):
        print(f"\n  [PARSER] Starting parse ({len(self.__tokens)} tokens)")
        result = self.__parse_program()
        print(f"  [PARSER] AST built:\n{result}\n")
        return result

    # Grammar rule methods

    # program ::= (account_number | exit), {command}
    def __parse_program(self):
        children   = []
        error_node = None
        token      = self.__current_token()

        # First token must be an account number or EXIT
        if token.get_type() == TOKEN_ACCOUNT_NUMBER:
            children.append(ASTNode("ACCOUNT_NUMBER", value=token.get_value()))
            print(f"  [PARSER] Account: {token.get_value()}")
            self.__consume()

        elif token.get_type() == TOKEN_EXIT:
            children.append(ASTNode("EXIT_PROGRAM"))
            self.__consume()

        else:
            error_node = ASTNode(
                "ERROR",
                value=f"Expected account number or EXIT, "
                      f"got '{token.get_value()}' ({token.get_type()})"
            )

        # Keep parsing commands until EOF or an error occurs
        if error_node is None:
            cmd_token = self.__current_token()
            while cmd_token.get_type() != TOKEN_EOF and error_node is None:
                command = self.__parse_command()
                if command.get_node_type() == "ERROR":
                    error_node = command
                else:
                    children.append(command)
                cmd_token = self.__current_token()

        if error_node is None:
            result = ASTNode("PROGRAM", children=children)
        else:
            result = error_node

        return result

    # command ::= deposit | withdrawal | check_balance |
    #             create_account | check_other_account | exit_program
    def __parse_command(self):
        token = self.__current_token()

        if token.get_type() == TOKEN_MENU_CHOICE:
            choice = token.get_value()
            self.__consume()
            print(f"  [PARSER] Menu choice: {choice}")
            result = self.__route_command(choice)

        elif token.get_type() == TOKEN_EXIT:
            self.__consume()
            result = ASTNode("EXIT_PROGRAM")

        else:
            result = ASTNode(
                "ERROR",
                value=f"Expected menu choice (1-6) or EXIT, "
                      f"got '{token.get_value()}' ({token.get_type()})"
            )

        return result

    # Routes menu choice digit to the correct grammar rule method
    def __route_command(self, choice):
        if choice == 1:
            result = self.__parse_deposit()
        elif choice == 2:
            result = self.__parse_withdrawal()
        elif choice == 3:
            result = self.__parse_check_balance()
        elif choice == 4:
            result = self.__parse_create_account()
        elif choice == 5:
            result = self.__parse_check_other_account()
        else:
            # choice == 6
            result = ASTNode("EXIT_PROGRAM")

        return result

    # deposit ::= "1", amount
    def __parse_deposit(self):
        amount_node = self.__expect_amount("DEPOSIT")
        if amount_node.get_node_type() == "ERROR":
            result = amount_node
        else:
            result = ASTNode("DEPOSIT", children=[amount_node])
            print(f"  [PARSER] Deposit amount: {amount_node.get_value()}")
        return result

    # withdrawal ::= "2", amount
    def __parse_withdrawal(self):
        amount_node = self.__expect_amount("WITHDRAWAL")
        if amount_node.get_node_type() == "ERROR":
            result = amount_node
        else:
            result = ASTNode("WITHDRAWAL", children=[amount_node])
            print(f"  [PARSER] Withdrawal amount: {amount_node.get_value()}")
        return result

    # check_balance ::= "3"  — no arguments needed
    def __parse_check_balance(self):
        print("  [PARSER] Check balance")
        return ASTNode("CHECK_BALANCE")

    # create_account ::= "4", name, name, account_number, amount
    def __parse_create_account(self):
        children   = []
        error_node = None

        # First name
        if error_node is None:
            node = self.__expect_name("CREATE first name")
            if node.get_node_type() == "ERROR":
                error_node = node
            else:
                children.append(ASTNode("FIRST_NAME", value=node.get_value()))
                print(f"  [PARSER] First name: {node.get_value()}")

        # Last name
        if error_node is None:
            node = self.__expect_name("CREATE last name")
            if node.get_node_type() == "ERROR":
                error_node = node
            else:
                children.append(ASTNode("LAST_NAME", value=node.get_value()))
                print(f"  [PARSER] Last name: {node.get_value()}")

        # Account number
        if error_node is None:
            token = self.__current_token()
            if token.get_type() == TOKEN_ACCOUNT_NUMBER:
                self.__consume()
                children.append(ASTNode("NEW_ACCT_NUM", value=token.get_value()))
                print(f"  [PARSER] New account number: {token.get_value()}")
            else:
                error_node = ASTNode(
                    "ERROR",
                    value=f"CREATE: expected account number, "
                          f"got '{token.get_value()}' ({token.get_type()})"
                )

        # Starting balance
        if error_node is None:
            node = self.__expect_amount("CREATE balance")
            if node.get_node_type() == "ERROR":
                error_node = node
            else:
                children.append(node)
                print(f"  [PARSER] Starting balance: {node.get_value()}")

        if error_node is None:
            result = ASTNode("CREATE_ACCOUNT", children=children)
        else:
            result = error_node

        return result

    # check_other_account ::= "5", account_number
    def __parse_check_other_account(self):
        token = self.__current_token()

        if token.get_type() == TOKEN_ACCOUNT_NUMBER:
            self.__consume()
            result = ASTNode("CHECK_OTHER_ACCOUNT", value=token.get_value())
            print(f"  [PARSER] Switch to account: {token.get_value()}")
        else:
            result = ASTNode(
                "ERROR",
                value=f"CHECK_OTHER_ACCOUNT: expected account number, "
                      f"got '{token.get_value()}' ({token.get_type()})"
            )

        return result

    # Helper methods

    # Read next token as an amount, return ERROR node if it isn't one
    def __expect_amount(self, context):
        token = self.__current_token()
        if token.get_type() == TOKEN_AMOUNT:
            self.__consume()
            result = ASTNode("AMOUNT", value=token.get_value())
        else:
            result = ASTNode(
                "ERROR",
                value=f"{context}: expected an amount, "
                      f"got '{token.get_value()}' ({token.get_type()})"
            )
        return result

    # Read next token as a name, return ERROR node if it isn't one
    def __expect_name(self, context):
        token = self.__current_token()
        if token.get_type() == TOKEN_NAME:
            self.__consume()
            result = ASTNode("NAME", value=token.get_value())
        else:
            result = ASTNode(
                "ERROR",
                value=f"{context}: expected a name, "
                      f"got '{token.get_value()}' ({token.get_type()})"
            )
        return result

    # Return current token without advancing
    def __current_token(self):
        return self.__tokens[self.__pos]

    # Return current token and advance the position by one
    def __consume(self):
        token = self.__tokens[self.__pos]
        if self.__pos < len(self.__tokens) - 1:
            self.__pos += 1
        return token
