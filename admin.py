from user import User
class Admin:
  def __init__(self) -> None:
    self.users = []
  def create_account(self,name,email,address,account_type):
    user = User(name,email,address,account_type)
    self.users.append(user)
    return user
  def delete_account(self,account_number):
    for user in self.users:
      if user.account_number == account_number:
        self.users.remove(user)
        print(f'Account with account number {account_number} has been deleted!!!')
        return
    print('Account not found')
  
  def show_all_accounts(self):
    for user in self.users:
      print(f"Name: {user.name}, Account Number: {user.account_number}, Balance: {user.balance}")
  
  def total_available_balance(self):
    total_balance = sum(user.balance for user in self.users)
    return total_balance
  
  def total_loan_amount(self):
    total_loan = sum(sum(user.transaction_history) for user in self.users if "Loan" in user.transaction_history)
    return total_loan
  def toggle_loan_feature(self, status):
    if status:
      User.take_loan = User.take_loan
      print("Loan feature is now enabled")
    else:
      User.take_loan = lambda self, amount: print('Loan feature is disabled')