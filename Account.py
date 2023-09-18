import random
import datetime
from Database import UserDatabase

#Database class form Databse.py
ud = UserDatabase()

class BankUser:
    user_count = 0

    #Initilize a bank user
    def __init__(self, account_type, balance, currency, owner):
        self.account_type = account_type
        self.balance = balance
        self.currency = currency
        self.owner = owner
        self.account_num = self.create_account_num()
        self.today = datetime.date.today()

    def create_account_num(self):
        base = 1234
        personal_nums = random.randint(1000, 9999)
        account_num = f"{personal_nums}{base}"
        return account_num
    
    def create_id(self):
        BankUser.user_count += 1
        return f"{self.owner[:3]}{BankUser.user_count}"

class GameUser(BankUser):

    #Initlize a Gameuser using inheritance from Bankuser
    def __init__(self,owner, username, password, friends ,account_type, balance=1, currency="NOK", gamebalance=0, savingsgoal=None):
        super().__init__(account_type, balance, currency, owner)
        self.username = username
        self.password = password
        self.gamebalance = gamebalance
        self.friends = friends
        self.savingsgoal = savingsgoal

    # Saves money to the account balance and saves the transaction to the database
    def save_money(self):
        savings_input = int(input("Savings amount: "))
        ratio = 0.01
        
        self.gamebalance = int(self.gamebalance)
        game_money_earned = int(savings_input * ratio)
    
        self.gamebalance += game_money_earned
        self.balance += savings_input

        self.set_goal()

        transaction_info = (
            self.create_id(),
            self.today,
            savings_input,
            self.currency,
            "Savings input",
            self.username,
            self.account_num,
        )

        #Saves transaction to database
        ud.new_transaction(transaction_info)

        return game_money_earned, transaction_info

    # The user can set a savingsgoal that when reached they get a in game reward
    def set_goal(self):
        goal = int(input("Set savings goal: "))
        reward_ratio = 0.05
        left_of_savingsgoal = goal - self.balance
        
        if goal > 0 and self.balance >= goal:
            reward = int(goal * reward_ratio)
            self.gamebalance += reward
            print(f"Congratulations! You have reached your savings goal. You receive a reward of {reward} GOLD!!")
        elif goal > 0:
            print(f"You have set a savings goal of {goal} NOK. Keep saving to reach your goal! Only {left_of_savingsgoal} left")
    
    def __str__(self):
        return f"""
            {self.account_type}
            {self.balance}
            {self.currency}
            {self.owner}
            {self.username}
            {self.password}
            {self.gamebalance}
            {self.friends}
            {self.account_num}
            {self.create_id()} 
            """

if __name__ == "__main__":
    pass
