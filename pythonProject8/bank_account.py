class Bank:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        self.is_active = True

    def name(self):
        print(f"Welcome{self.account_holder}")

    def deposit(self, amount):
        if amount > 0 :
            self.balance += amount
            print(f"Your bank balance is{self.balance}.")

    def withdraw(self, amount):
        if self.balance >= amount and self.is_active:
            self.balance -= amount

    def check_balance(self):
        print(f"Your bank balance is{self.balance}.")

    def deactivate(self):
        if self.is_active:
            self.is_active = False
            print("Your account is deactivated seek help")
        else:
            print("Can't drive. The engine is off.")

    def account_summary(self):
        print(f"{self.account_holder},{self.is_active},{self.balance}")

my_account = Bank("Peter Muigai")
my_account.deposit(1000)
my_account.withdraw(300)
my_account.check_balance()
my_account.account_summary()
my_account.deactivate()
my_account.withdraw(100)
my_account.account_summary()
