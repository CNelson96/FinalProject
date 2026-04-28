import re


class BankAccount:

    #Constructor for bank account#
    def __init__(self, first_name, last_name, acct_num, balance):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_acct_num(acct_num)
        self.set_balance(balance)


    # Getters##


    def get_first_name(self):
        return self.__first_name


    def get_last_name(self):
        return self.__last_name


    def get_acct_num(self):
        return self.__acct_num

    def get_balance(self):
        return self.__balance



    # Setters #


    #Function for setting up the customers first name
    def set_first_name(self, first_name):

        #Validation for first name being blank#
        if first_name.strip() == "":
            print("First name cannot be blank")
        else:
            self.__first_name = first_name

    # Function for setting up the customers last name
    def set_last_name(self, last_name):

        # Validation for last name being blank#
        if last_name.strip() == "":
            print("Last name cannot be blank")

        else:
            self.__last_name = last_name


    #Function to set the account number using regEx
    def set_acct_num(self, acct_num):
        pattern = r"^[A-Za-z]{2}[0-9]{6}$"

        #if the pattern matches the regex
        if re.fullmatch(pattern, acct_num):


            valid_initials = self.__first_name[0] + self.__last_name[0]

            #Validate that acct num matches customers initials
            if acct_num[:2].upper() == valid_initials.upper():
                self.__acct_num = acct_num

            else:
                print("Account initials don't match customer's name")


        else:
            print("Invalid account number.")



    #Function to set the balance of the account
    def set_balance(self, balance):

        #Validation to not allow balance to be negative
        if balance < 0:
            print("Balance can't be negative")

        else:
            self.__balance = balance





    #Function for withdrawal#
    def withdrawal(self, amount):

        result = self.__balance

        # If amount chosen is greater than balance, reject it
        if amount > self.__balance:
            print("Insufficient Funds, you are attempting to withdraw more than your current balance of $" +
                  f"{self.__balance:.2f}")

        # Amount must be a positive number
        elif amount <= 0:
            print("Amount must be greater than 0.")

        # update balance with new balance
        else:
            self.__balance -= amount
            print("You withdrew $" +  f"{amount:.2f}" + ". Your new balance is $" + f"{self.__balance:.2f}")
            result = self.__balance

        return result


    # Function for deposit#
    def deposit(self, amount):

        result = self.__balance

        #amount deposited has to be a positive integer#
        if amount <= 0:
            print("Deposit must be a number greater than 0")

        # update balance with money that was deposited
        else:
            self.__balance += amount
            print("You deposited $" + f"{amount:.2f}" + ". Your new balance is $" + f"{self.__balance:.2f}")
            result = self.__balance

        return result

