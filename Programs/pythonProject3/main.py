class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount} to {self.owner}'s account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount} from {self.owner}'s account.")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

acc = BankAccount("Peter", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())