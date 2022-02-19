class Bankaccounts:
    accounts = []
    def __init__(self,intrate,balance):
        self.intrate = intrate
        self.balance = balance
        Bankaccounts.accounts.append(self)

    def deposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging 5$ fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        return f"{self.balance}"


    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.intrate)
        return self

    @classmethod
    def printallacc(cls):
        for account in cls.accounts:
            account.display_account_info()

class user:
    def __init__(self,name):
        self.name = name
        self.account = { 
            "checking":Bankaccounts(.01,500),
            "savings":Bankaccounts(.02,500)
        }

    def make_deposit(self,amount):
        self.amount += amount
        return self

    def make_withdrawal(self,amount):
        self.amount -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

Nick = user("Nick")
Nick.account["checking"].deposit(200)
Nick.display_user_balance()
