class BankAccount:
    def __init__(self, name, secret, balance):
        self.name = name
        self.__secret = secret
        self.__balance = balance

    def check_balance(self, secret):
        if secret == self.__secret:
            print(self.name, "balance:", self.__balance)
        else:
            print("Invalid secret number")

    def deposit(self, amount, secret):
        if secret == self.__secret:
            if amount < 0:
                print("Invalid amount")
            else:
                self.__balance += amount
                print("Deposit success.")
                print(self.name, "remaining balance is:", self.__balance)
        else:
            print("Invalid secret number")

    def withdraw(self, secret, amount):
        if secret == self.__secret:
            remain = self.__balance - amount
            if remain < 0:
                print("Not enough money")
            else:
                self.__balance = remain
                print("Withdraw successfully.")
                print(self.name, "remaining balance is:", self.__balance)
        else:
            print("Invalid secret number")

    # add receive 
    def receive(self, amount, from_account):
        if from_account:
            self.__balance += amount
        else:
            print("Failed")

    def transfer(self, amount, transfer_to, secret):
        if secret == self.__secret:
            remain = self.__balance - amount
            if remain < 0:
                print("Not enough money")
            else:
                transfer_to.receive(amount=amount, from_account=self)
                self.__balance = remain
                print("Transfer successfully to", transfer_to.name)
                print(self.name, "remaining balance is:", self.__balance)
        else:
            print("Invalid secret")

    def pay_service(self, secret, service_name, amount):
        if secret == self.__secret:
            remain = self.__balance - amount
            if remain < 0:
                print("Not enough money")
            else:
                self.__balance = remain
                print("Paid", amount, "for", service_name)
                print(self.name, "remaining balance is:", self.__balance)
        else:
            print("Invalid secret")

class StudentBankAccount(BankAccount):
    def withdraw(self, secret, amount):
        if amount > 500:
            print("Student cannot withdraw more than $500")
        else:
            super().withdraw(secret, amount)



# Saving Account
class SavingAccount(BankAccount):
    def add_interest(self):
        self._BankAccount__balance += 10
        print("Interest added.")
        print("Balance:", self._BankAccount__balance)



# Premium Saving

class PremiumSaving(SavingAccount):
    def deposit(self, amount, secret):
        if secret == self._BankAccount__secret:
            if amount < 0:
                print("Invalid amount")
            else:
                super().deposit(amount, secret)
                cashback = amount * 0.02
                self._BankAccount__balance += cashback
                print("2% cashback:", cashback)
                print("Balance:", self._BankAccount__balance)
        else:
            print("Invalid secret number")



# Business Acc
class BusinessAccount(BankAccount):
    def take_loan(self, amount):
        if amount > 0:
            self._BankAccount__balance += amount
            print("Loan received:", amount)
            print("Balance:", self._BankAccount__balance)
        else:
            print("Invalid amount")



# Create Friend Acc

def create_friend_account():
    friend_name = input("Enter friend's name: ")
    default_balance = 5000
    default_secret = "000"  

    print("Friend account created with balance:", default_balance)

    return BankAccount(friend_name, default_secret, default_balance)

#input systerm
print(" BANK ATM SYSTEM ")

while True:

    print("\nChoose account type")
    print("1. Normal")
    print("2. Student")
    print("3. Premium Saving")
    print("4. Business")
    print("0. Exit program")

    account_type = input("Select: ")

    if account_type == "0":
        print("Program stopped")
        break

    user_name = input("Name: ")
    user_secret = input("secret Number: ")
    initial_balance = float(input("Money: "))

    if account_type == "1":
        my_account = BankAccount(user_name, user_secret, initial_balance)
    elif account_type == "2":
        my_account = StudentBankAccount(user_name, user_secret, initial_balance)
    elif account_type == "3":
        my_account = PremiumSaving(user_name, user_secret, initial_balance)
    elif account_type == "4":
        my_account = BusinessAccount(user_name, user_secret, initial_balance)
    else:
        print("Invalid choice")
        continue

    # Create friend acc
    friend_account = create_friend_account()

   
    while True:

        print("\n MENU ")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Pay service")

        if isinstance(my_account, SavingAccount):
            print("6. Add interest")

        if isinstance(my_account, BusinessAccount):
            print("7. Take loan")

        print("0. Logout")

        menu_choice = input("Choose: ")

        if menu_choice == "1":
            sec = input("Secret: ")
            my_account.check_balance(sec)

        elif menu_choice == "2":
            sec = input("Secret: ")
            amount = float(input("Amount: "))
            my_account.deposit(amount, sec)

        elif menu_choice == "3":
            sec = input("Secret: ")
            amount = float(input("Amount: "))
            my_account.withdraw(sec, amount)

        elif menu_choice == "4":
            sec = input("Secret: ")
            amount = float(input("Amount: "))
            my_account.transfer(amount, friend_account, sec)

        elif menu_choice == "5":
            sec = input("Secret: ")
            service = input("Service: ")
            amount = float(input("Amount: "))
            my_account.pay_service(sec, service, amount)

        elif menu_choice == "6" and isinstance(my_account, SavingAccount):
            my_account.add_interest()

        elif menu_choice == "7" and isinstance(my_account, BusinessAccount):
            amount = float(input("Loan amount: "))
            my_account.take_loan(amount)

        elif menu_choice == "0":
            print("Logout...")
            break

        else:
            print("Invalid choice")