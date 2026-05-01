# I certify that the Python file I am submitting is all my own work.
# None of it is copied from any source or any person.
# Signed: Cory Nelson, Marcus Her, Nou Chai Thao.
# Date: 5/01/2026
#
# Author: Cory Nelson, Marcus Her, Nou Chai Thao.
# Date:  5/01/2026
# Class: CSS335
# Assignment: Final Project Banking
# File Name: Lexer.py
# Description: Creating the lexer for the banking program
#





import re
from Token import (Token, TOKEN_ACCOUNT_NUMBER, TOKEN_MENU_CHOICE,
                   TOKEN_AMOUNT, TOKEN_NAME, TOKEN_EXIT,
                   TOKEN_EOF, TOKEN_INVALID)

# Breaks the input string into tokens by splitting on whitespace
# and classifying each word using regex patterns from the EBNF
class Lexer:

    # Compiled regex patterns — built once at the class level
    _PAT_ACCOUNT_NUMBER = re.compile(r'^[A-Za-z]{2}[0-9]{6}$')  # ex CN123456
    _PAT_MENU_CHOICE    = re.compile(r'^[1-6]$')                 # single digit 1-6
    _PAT_AMOUNT         = re.compile(r'^\d+(\.\d+)?$')           # ex 500.00
    _PAT_NAME           = re.compile(r'^[A-Za-z]+$')             # letters only

    # Store the raw input string and prepare an empty token list
    def __init__(self, source):
        self.__source = source.strip()
        self.__tokens = []

    # Split the source on whitespace and classify each word as a Token.
    # Appends an EOF token at the end as a stream terminator.
    def tokenize(self):
        words = self.__source.split()
        index = 0

        while index < len(words):
            token = self.__classify_word(words[index])
            self.__tokens.append(token)
            print(f"  [LEXER] {token}")
            index += 1

        # Mark the end of the token stream
        eof = Token(TOKEN_EOF, None)
        self.__tokens.append(eof)
        print(f"  [LEXER] {eof}")

        return self.__tokens

    def get_tokens(self):
        return self.__tokens

    # Print the token list in a formatted table
    def print_tokens(self):
        print("\n--- LEXER OUTPUT ---")
        print(f"{'Index':<8}{'Type':<20}{'Value'}")
        print("-" * 42)
        index = 0
        while index < len(self.__tokens):
            t = self.__tokens[index]
            print(f"{index:<8}{t.get_type():<20}{t.get_value()}")
            index += 1
        print("--- END LEXER OUTPUT ---\n")

    # Determine the token type for a single word.
    def __classify_word(self, word):
        upper_word = word.upper()

        # EXIT keyword must come before the name check
        if upper_word == "EXIT":
            result = Token(TOKEN_EXIT, "EXIT")

        # Account number (2 letters + 6 digits) before plain name check
        elif self._PAT_ACCOUNT_NUMBER.match(word):
            result = Token(TOKEN_ACCOUNT_NUMBER, upper_word)

        # Single digit 1-6 is a menu choice, stored as int
        elif self._PAT_MENU_CHOICE.match(word):
            result = Token(TOKEN_MENU_CHOICE, int(word))

        # Dollar amount stored as float for arithmetic
        elif self._PAT_AMOUNT.match(word):
            result = Token(TOKEN_AMOUNT, float(word))

        # Letters-only word used for first or last names
        elif self._PAT_NAME.match(word):
            result = Token(TOKEN_NAME, word)

        # Nothing matched — flag as invalid
        else:
            result = Token(TOKEN_INVALID, word)

        return result
