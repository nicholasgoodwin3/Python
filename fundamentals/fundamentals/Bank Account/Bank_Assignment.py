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
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.intrate)
        return self

    @classmethod
    def printallacc(cls):
        for account in cls.accounts:
            account.display_account_info()

checking = Bankaccounts(.01,500)
savings = Bankaccounts(.02,500)

checking.deposit(5).deposit(10).deposit(15).withdraw(85).yield_interest().display_account_info()
savings.deposit(10).deposit(20).withdraw(40).withdraw(50).withdraw(100).yield_interest().display_account_info()

Bankaccounts.printallacc() ## 


