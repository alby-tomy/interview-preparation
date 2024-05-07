class BankAccount:
    def __init__(self, account, balance, owner_name):
        self.account = account
        self.balance = balance
        self.owner_name = owner_name

    def deposit(self, amount):
        self.balance += amount
        print("Deposit of ",amount, "successful.")
        self.display_balance()

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print("Withdrawl of", amount, "successful.")
            self.display_balance()

    def display_balance(self):
        print("Account balance : ", self.balance)


account = BankAccount("123456789", 1000, "John Doe")
account.deposit(500)
account.withdraw(200)
