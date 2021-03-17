car = {
    'make': 'Rolls Royce',
    'model': 'Ghost',
    'color': 'white'
}

class CoffeeCup():  #Similar to constructor in JS

    def __init__(self, capacity):
        self.capacity = capacity 
        self.amount = 0

    def fill(self): # method on CoffeeCup
        self.amount = self.capacity

    def empty(self): # method on CoffeeCup
        self.amount = 0 

    def drink(self, amount): # method
        self.amount -= amount     # Find related code in python classes inheritance


#2 - Understand how classes are defined
#3 - Understand how objects are initialized
#4 - Understand instance variables and instance methods

steves_cup = CoffeeCup(12)  # a fancy latte.
seans_cup = CoffeeCup(16)    # gas station drip.
brandis_cup = CoffeeCup(2)  # a quick espresso.

steves_cup.fill()
print(steves_cup.amount)
# print(help(steves_cup))

class BankAccount():

    def __init__(self, kind, balance):
        self.kind = kind
        self.balance = balance
        self.overdraft_fees = 0

    def __str__(self):
        return f"Bank Account that has ${self.balance}"

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
        if (self.balance < 0):
            self.overdraft_fees += 20
        return amount

checkingAct = BankAccount('checking', 200)
savingsAct = BankAccount('savings', 4000)

print(checkingAct.deposit(15))