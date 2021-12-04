#Learning classes OOP 
#creating the class
class User:
    def __init__(self, username, email_address):
        self.username = username
        self.email_address = email_address
        self.account_balance = 0 #I dont need this as my parameter because its gonna be the same for every user starting out and every user will have a bank account 
    def deposit(self, amount):     # Added deposit method 
        self.account_balance += amount
        return self
    def withdrawal(self, amount):  #added a withdrawal method 
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"{self.username} Your Balance is {self.account_balance}")
    def tranfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount 
        print(f"{self.username} Your balance is {self.account_balance}")
        print(f"{other_user.username} Your balance is {other_user.account_balance}")
    
    
caden = User("Caden Wilcox", "wilcox4357@gmail.com")
alex = User("Alex Kanan", "alex@email.com")
alex.deposit(600)
alex.display_user_balance()
caden.deposit(400).withdrawal(200).display_user_balance()
caden.tranfer_money(alex, 100)
