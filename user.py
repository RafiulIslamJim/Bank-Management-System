import random
class User:
  def __init__(self,name,email,address,account_type) -> None:
    self.name = name
    self.email = email
    self.address = address
    self.account_type = account_type
    self.balance = 0
    self.account_number = random.randint(100000,999999)
    self.transaction_history = []

  def deposit(self,amount):
    self.balance += amount
    self.transaction_history.append(f'Deposit: +{amount}')
  def withdraw(self,amount):
    if self.balance >= amount:
      self.balance -= amount
      self.transaction_history.append(f'Withdrawal: -{amount}')
    else:
      print('Withdrawal amount exceeded')
  
  def check_balance(self):
    return self.balance
  def transfer(self,amount,recipient):
    if self.balance >= amount:
      self.balance -= amount
      recipient.balance += amount
      self.transaction_history.append(f'Transfer: -{amount} to {recipient.name}')
      recipient.transaction_history.append(f'Transfer: +{amount} from {self.name}')
    else:
      print('Insufficient funds for transfer')
  def take_loan(self,amount):
    if len(self.transaction_history) < 2:
      self.balance += amount
      self.transaction_history.append(f'Loan: +{amount}')
    else:
      print('You have already taken the maximum number of loans')
  def show_transaction_history(self):
    for transaction in self.transaction_history:
      print(transaction)
  