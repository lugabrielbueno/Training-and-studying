class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return f'Account owner: {self.owner.title()}\nAccount balance: ${self.balance}'
    def deposit(self,amount):
        self.balance += amount
        print('${} succefully deposited'.format(str(amount)))
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print('${}. Take your money'.format(str(amount)))
        else:
            print('Funds Unavailable')