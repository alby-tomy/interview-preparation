class BankAccount:
    def __init__(self, account_number, balance, owner_name):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name

    def deposit(self, amount):
        self.balance += amount
        print("Deposit of", amount, "successful.")
        self.display_balance()

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print("Withdrawal of", amount, "successful.")
            self.display_balance()

    def display_balance(self):
        print("Account Balance:", self.balance)

# Example usage:
account = BankAccount("123456789", 1000, "John Doe")
account.deposit(500)
account.withdraw(200)

