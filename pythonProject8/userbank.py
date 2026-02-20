class BankAccount:
    def __init__(self, account_holder, account_number):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = 0
        self.is_active = True

    def deposit(self, amount):
        if amount > 0 and self.is_active:
            self.balance += amount
            print(f"Deposited Ksh{amount}. Your balance is now Ksh{self.balance}.")
        else:
            print("Deposit failed. Ensure amount is positive and account is active.")

    def withdraw(self, amount):
        if not self.is_active:
            print("Withdrawal failed. Your account is deactivated.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew Ksh{amount}. New balance: Ksh{self.balance}.")

    def check_balance(self):
        print(f"Current balance: Ksh{self.balance}.")

    def deactivate(self):
        if self.is_active:
            self.is_active = False
            print("Account has been deactivated. Please contact the bank.")
        else:
            print("Account is already deactivated.")

    def account_summary(self):
        status = "Active" if self.is_active else "Deactivated"
        print("\n--- Account Summary ---")
        print(f"Holder: {self.account_holder}")
        print(f"Account No: {self.account_number}")
        print(f"Balance: Ksh{self.balance}")
        print(f"Status: {status}")
        print("------------------------")

# 🧾 User input
account_holder = input("Enter account holder name: ")
account_number = input("Enter account number: ")

my_account = BankAccount(account_holder, account_number)

# Test some actions
my_account.deposit(1500)
my_account.withdraw(500)
my_account.account_summary()
