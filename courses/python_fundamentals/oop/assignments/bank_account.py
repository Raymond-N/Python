class BankAccount:

    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdrawal(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
        return self

    def display_account_info(self):
        print("===============")
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all(cls):
        for account in cls.all_accounts:
            account.display_account_info()



bank_account_1 = BankAccount(0.01, 100)
bank_account_2 = BankAccount(0.04, 400)

bank_account_1.deposit(50).deposit(75).deposit(180).withdrawal(25).yield_interest().display_account_info()
bank_account_2.deposit(25).deposit(50).withdrawal(25).withdrawal(50).withdrawal(75).withdrawal(100).yield_interest().display_account_info()

BankAccount.print_all()