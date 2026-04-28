# Token type constants — ALL_CAPS means treat as constants
TOKEN_ACCOUNT_NUMBER = "ACCOUNT_NUMBER"  # e.g. CN123456
TOKEN_MENU_CHOICE    = "MENU_CHOICE"     # digits 1-6
TOKEN_AMOUNT         = "AMOUNT"          # e.g. 500.00
TOKEN_NAME           = "NAME"            # letters only, e.g. John
TOKEN_EXIT           = "EXIT"            # the word EXIT
TOKEN_EOF            = "EOF"             # end of token stream
TOKEN_INVALID        = "INVALID"         # unrecognized input

# Represents one classified unit from the input string
class Token:

    # Store the token type and value privately
    def __init__(self, token_type, value):
        self.__token_type = token_type
        self.__value      = value

    # Getters

    def get_type(self):
        return self.__token_type

    def get_value(self):
        return self.__value

    # Readable output when printing a token
    def __repr__(self):
        return f"Token({self.__token_type}, {self.__value})"