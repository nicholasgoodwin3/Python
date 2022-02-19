class user:

    def __init__(self,name):
        self.name = name
        self.amount = 0

    def make_deposit(self,amount):
        self.amount += amount

    def make_withdrawal(self,amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User:{self.name},balance:{self.amount}")

    def transfer_money(self,amount,user):
        self.amount += amount
        user.amount -= amount
        self.display_user_balance
        user.display_user_balance

Nick = user("Nick")
Amy = user("Amy")
Pants = user("Pants")
Poe = user("Poe") ## cant leave out my other cat so... 4 classes.

Nick.make_deposit(1000)
Nick.make_deposit(10)
Nick.make_deposit(5)
Nick.make_withdrawal(515)
Nick.display_user_balance()

Amy.make_deposit(8)
Amy.make_deposit(10)
Amy.make_withdrawal(2)
Amy.make_withdrawal(5)
Amy.display_user_balance()

Pants.make_deposit(50)
Pants.make_withdrawal(10)
Pants.make_withdrawal(5)
Pants.make_withdrawal(10)
Pants.display_user_balance()

Nick.transfer_money(200,Amy)

