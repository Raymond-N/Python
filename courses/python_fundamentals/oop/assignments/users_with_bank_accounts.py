class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = BankAccount(int_rate=0.02,balance=0)

    def display_info(self):
        print("=========================")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards member: {self.is_rewards_member}")
        print(f"Gold card points: {self.gold_card_points}")
    
    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member.")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
    
    def spend_points(self,amount):
        if self.gold_card_points - amount < 0:
            print("Not enough points!")
        else:
            self.gold_card_points = self.gold_card_points - amount

    def make_deposit(self,amount):
        self.account.deposit(amount)

    def make_withdrawal(self,amount):
        self.account.withdrawal(amount)

    def display_user_balance(self):
        print(f"{self.first_name} {self.last_name}'s account balance: {self.account.balance}")
        print("==================")

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

user_1 = User("Raymond", "Natividad", "raymond@email.com", 29)
user_2 = User("Karina", "Moreno", "karina@email.com",25)
user_3 = User("Anthony", "Villacis", "anthony@email.com", 35)

# user_1.enroll()
# user_1.spend_points(50)
# user_1.display_info()
# user_1.enroll()
user_1.make_deposit(300)
user_1.make_deposit(300)
user_1.make_deposit(300)
user_1.make_withdrawal(150)
user_1.display_user_balance()

# user_2.enroll()
# user_2.spend_points(80)
# user_2.display_info()
user_2.make_deposit(250)
user_2.make_deposit(300)
user_2.make_withdrawal(500)
user_2.make_withdrawal(150)
user_2.display_user_balance()

# user_3.display_info()
# user_3.spend_points(40)
user_3.make_deposit(300)
user_3.make_deposit(300)
user_3.make_deposit(300)
user_3.make_withdrawal(150)
user_3.display_user_balance()

# bank_account_1 = BankAccount(0.01, 100)
# bank_account_2 = BankAccount(0.04, 400)

# bank_account_1.deposit(50).deposit(75).deposit(180).withdrawal(25).yield_interest().display_account_info()
# bank_account_2.deposit(25).deposit(50).withdrawal(25).withdrawal(50).withdrawal(75).withdrawal(100).yield_interest().display_account_info()