class BankAccount:

    all_accounts = []

    def __init__(self, int_rate, balance, account_type="Checking"):
        self.int_rate = int_rate
        self.balance = balance
        self.account_type = account_type
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
        print(f"{self.account_type} Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all(cls):
        for account in cls.all_accounts:
            account.display_account_info()

# bank_account_1 = BankAccount(0.01, 100, "Checking")
# bank_account_2 = BankAccount(0.04, 400, "Savings")

# bank_account_1.deposit(50).deposit(75).deposit(180).withdrawal(25).yield_interest().display_account_info()
# bank_account_2.deposit(25).deposit(50).withdrawal(25).withdrawal(50).withdrawal(75).withdrawal(100).yield_interest().display_account_info()

# BankAccount.print_all()

class User:

    all_users = []

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = BankAccount(int_rate=0.02, balance=0)
        User.all_users.append(self)

    # def enroll(self):
    #     if self.is_rewards_member == True:
    #         print("User already a member.")
    #     else:
    #         self.is_rewards_member = True
    #         self.gold_card_points = 200
    
    # def spend_points(self,amount):
    #     if self.gold_card_points - amount < 0:
    #         print("Not enough points!")
    #     else:
    #         self.gold_card_points = self.gold_card_points - amount

    def open_new_account(self, int_rate, balance, account_type):
        print("===========================")
        print(f"Opening new {self.account.account_type} account.")
        self.account = BankAccount(int_rate, balance, account_type)

    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdrawal(self, amount):
        self.account.withdrawal(amount)

    def display_user_balance(self):
        print(f"{self.first_name}, {self.account.account_type} balance: {self.account.balance}")

user_1 = User("Raymond", "Natividad", "natividad2315@gmail.com", 29)

# user_1.display_user_balance()
# user_1.make_deposit(500)
# user_1.make_deposit(500)
# user_1.make_deposit(500)
# user_1.make_withdrawal(750)
user_1.open_new_account(0.04, 400, "Checking")
user_1.display_user_balance()
user_1.open_new_account(0.02, 800, "Savings")
user_1.display_user_balance()
