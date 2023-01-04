class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

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

user_1 = User("Raymond", "Natividad", "raymond@email.com", 29)
user_2 = User("Karina", "Moreno", "karina@email.com",25)
user_3 = User("Anthony", "Villacis", "anthony@email.com", 35)

user_1.enroll()
user_1.spend_points(50)
user_1.display_info()
user_1.enroll()
user_2.enroll()
user_2.spend_points(80)
user_2.display_info()
user_3.display_info()
user_3.spend_points(40)