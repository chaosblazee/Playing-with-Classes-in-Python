class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display(self):
        # print("\n Available Balance =", self.account_balance)
        print(f"User: {self.name} , Balance: {self.account_balance}")

michael = User("michael")
sarah = User("sarah")
joe = User("joe")

michael.make_deposit(300)
michael.make_deposit(800)
michael.make_deposit(700)
michael.make_withdrawal(200)
michael.display()

sarah.make_deposit(500)
sarah.make_deposit(900)
sarah.make_deposit(200)
sarah.make_deposit(700)
sarah.display()

joe.make_deposit(1300)
joe.make_withdrawal(100)
joe.make_withdrawal(250)
joe.make_withdrawal(75)
joe.display()