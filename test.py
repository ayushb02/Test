
class BankAccount:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
      
 # This fuction will update the account in the event of deposit
    def deposit(self, amount):
        self.balance += amount
        return self.balance
      
  # This fuction will update the account in the event of withdrawal
    def withdraw(self, amount):
        if amount > self.balance:
            print('Balance is not sufficient.')
        else:
            self.balance -= amount
        return self.balance
 

account = BankAccount('John Doe', 100.5)
print(account.deposit(30))
print(account.withdraw(50))
print(account.withdraw(100))
