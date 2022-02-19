class user:

    def __init__(self,name):
        self.name = name
        self.amount = 0

    def make_deposit(self,amount):
        self.amount += amount
        return self

    def make_withdrawal(self,amount):
        self.amount -= amount
        return self

    def display_user_balance(self):
        print(f"User:{self.name},balance:{self.amount}")
        return self

    def transfer_money(self,amount,user):
        self.amount += amount
        user.amount -= amount
        self.display_user_balance
        user.display_user_balance
        return self

Nick = user("Nick")
Amy = user("Amy")
Pants = user("Pants")
Poe = user("Poe") ## cant leave out my other cat so... 4 classes.

Nick.make_deposit(1000).make_deposit(10).make_deposit(5).make_withdrawal(515).display_user_balance()

Amy.make_deposit(8).make_deposit(10).make_withdrawal(2).make_withdrawal(5).display_user_balance()

Pants.make_deposit(50).make_withdrawal(10).make_withdrawal(5).make_withdrawal(10).display_user_balance()

Nick.transfer_money(200,Amy)

