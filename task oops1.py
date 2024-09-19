class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self._balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Rs {amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
                print(f"Rs {amount} withdrawn successfully.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        return f"Current balance: Rs {self._balance}"


account = BankAccount("sahanabi", 1000)

account.deposit(50)

account.withdraw(30)

print(account.check_balance())

account.withdraw(200)

account.withdraw(1000)

print(account.check_balance())
