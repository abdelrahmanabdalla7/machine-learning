class bank:
    def __init__(self,users=dict,logged_in_user=dict,balance=float):
        self.users = users
        self.logged_in_user = logged_in_user
        self.balance= balance
    def register (self,username,password):
        if username in self.users:
            print ("username is already exist, please choose another id")
        else:
            if len (username) and len (password) <= 8 :
                print ("username and password should be at least 9 characters long") 
                exit ()
            else:
                self.users[username] = {"password":password , "balance":0}
                print (f"user: {username} created successfully")
                return print (self.users)

    def login (self,username,password):
        if username in self.users and self.users[username]["password"] == password :
            self.logged_in_user = username
            print (f"welcome {username}")
            return True
        else:
            print("Invalid username or password")
            return False

    def check_balance (self):
        if self.logged_in_user:
            balance = self.users[self.logged_in_user]["balance"]
            print(f"Your current balance is: {balance}")
        else:
            print("Please login first")
    
    def deposit (self, amount):
        if self.logged_in_user:
            if amount > 0:
                self.users[self.logged_in_user]["balance"] += amount
                print(f"Deposited {amount}, your new balance is: {self.users[self.logged_in_user]['balance']}")
            else:
                print("Deposit amount should be positive")
        else:
            print("Please login first")
    
    def withdraw (self, amount):
        if self.logged_in_user:
            if amount > 0 and amount <= self.users[self.logged_in_user]["balance"]:
                self.users[self.logged_in_user]["balance"] -= amount
                print(f"Withdrew {amount}, your new balance is: {self.users[self.logged_in_user]['balance']}")
            else:
                print("Withdraw amount should be positive and not exceed your balance")
        else:
            print("Please login first")

    def get_user_count (self):
        return len(self.users)