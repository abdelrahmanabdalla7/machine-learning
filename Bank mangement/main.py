from bankmanger import bank
user1=bank ({},{},)


while True:
    print("welcome to the bank manger system\n1-register a new account\n2-login")
    choice=int(input("enter your choice: "))
    if choice==1:
        register_username=input ("username: ")
        register_password=input ("password: ")
        user1.register(register_username,register_password)
    elif choice==2:
        login_username=input ("login username: ")
        login_password=input ("login password: ")
        if user1.login (login_username,login_password):
            print("\n1-check balance\n2-deposit\n3-withdraw\n4-logout")
            while True:
                
                choice=int(input("enter your choice: "))
                if choice==1:
                    user1.check_balance()
                elif choice==2:
                    deposit_amount=float(input("enter the amount to deposit: "))
                    user1.deposit(deposit_amount)
                elif choice==3:
                    withdraw_amount=float(input("enter the amount to withdraw: "))
                    user1.withdraw(withdraw_amount)
                elif choice==4:
                    break
                else:
                    print("invalid choice")
                    continue
