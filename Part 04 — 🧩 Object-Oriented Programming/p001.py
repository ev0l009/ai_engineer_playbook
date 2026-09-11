class Wallet:
  def __init__(self):
    self.users = []
  def __len__(self):
    return len(self.users)
  def register_user(self):
    print('\nUSER REGISTRATION')
    username=input('Username:  ')
    password=input('Password:  ')
    if not username and not password:
      print('Registeration Failed...')
      return
    user = User(username,password)
    self.users.append(user)
    print('Registeration successful!')
  def login(self):
    print('\nUSER SIGN IN')
    username=input('Username:  ')
    password=input('Password:  ')
    for user in self.users:
      if user.username==username and user.password==password:
        print('Login successful!')
        return user
    print('\nInvalid credentials...')
    return
    

class User:
  def __init__(self,username,password):
    self.username=username
    self.password=password
    self.balance=0
  def check_balance(self):
    print(f'Your balance is {self.balance}CRD.')
  def withdraw(self):
    amt=input('Amount: ')
    if amt <= self.balance:
      self.balance -= amt
      print(f'Withdrawal successful. \nYour current balance is {self.balance}')
      return self
    print('Withdrawal Failed')
    return self
  def deposit(self):
    amt=input('Amount: ')
    if amt > 0.5:
      self.balance += amt
      print(f'Deposit successful. \nYour current balance is {self.balance}')
      return self
    print('Deposit Failed')
    return self
  def __str__(self):
    print('\nUSER PROFILE')
    print(f'Username: {self.username}')