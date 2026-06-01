class InsufficientFundsError(Exception):
    pass
class bankaccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
        self.history=[]
    def deposit(self,amount):
        self.balance+=amount
        self.history.append(f"deposit : {amount}")
    def withdraw(self,amount):
        if(amount>self.balance):
            raise InsufficientFundsError("insufficient balance")
        self.balance -= amount
        self.history.append(f"withdraw : {amount}")
    def get_balance(self):
        return self.balance
    def transaction_history(self):
        for transaction in self.history:
            print(transaction)
    def __str__(self):
        return f"owner : {self.owner} balance : {self.balance}"
class savingsaccount(bankaccount):
    def __init__(self,owner,balance,intereset_rate):
        super().__init__(owner,balance)
        self.interest_rate = intereset_rate
    def apply_interest(self):
        interest = self.balance * self.interest_rate /100
        self.balance+=interest
        self.history.append(f"interest : {interest}")

class currentaccount(bankaccount):
    def __init__(self, owner, balance,overdraft_limit):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit
    def withdraw(self, amount):
        if(self.balance-amount <- self.overdraft_limit):
            raise InsufficientFundsError("overdraft_limit execeeded")
        self.balance-=amount
        self.history.append(f"withdraw : {amount}")

print("\n BANK ACCOUNTS")
acc = bankaccount("sanju",10000)
acc.deposit(5000)
acc.withdraw(100)
print(acc)
print("balance : ",acc.get_balance())

print("\n transaction_history")
acc.transaction_history()

print("\n SAVINGS ACCOUNT")
sav=savingsaccount("saya",50000,2)

print("before interest :",sav.get_balance())
sav.apply_interest()
print("after interest :",sav.get_balance())

print("\n transaction_history")
sav.transaction_history()

print("CURRENT ACCOUNT")
cur=currentaccount("jerry",10000,2000)
cur.withdraw(4000)
print(cur)
print("balance : ",cur.get_balance())

print("\n transaction history")
cur.transaction_history()

print("\n error test")
try:
    acc.withdraw(5000)
except InsufficientFundsError as e:
    print("error :",e)

try:
    cur.withdraw(2000)
except InsufficientFundsError as e:
    print("error :",e)            





