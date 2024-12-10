from librarymanger import Library
import time

lib=Library(["COD Mobile", "PUBG Mobile", "Free Fire", "Hopeless"],{},{})


while True:
    print("Welcome to the Library Management System")
    print("1- see the game list")
    print("2- Rent a game")
    print("3- return a game")
    print("4- donate a game")
    print("5. Exit")

    choice=int(input("Enter your choice: "))

    if choice == 1:
        print("\nAvailable Games")
        print(lib.games())

    elif choice == 2:
        print(lib.games())
        name=input("Enter your name? ")
        gamename=input("Enter game name? ")
        lib.lend(name=name, gamename=gamename)

    elif choice == 3:
        if len (lib.lender)>0:
            print(lib.lender)
            name=input("Enter your name: ")
            gamename=input("Enter game name: ")        
            lib.returnb(name=name, gamename=gamename)
        else:
            print("No one is borrowing any game.")

    elif choice == 4:
        doner=input("Enter your name: ")
        newgame=input("Enter game name: ") 
        lib.donate(doner=doner,newgame=newgame)

    elif choice == 5:
        print("Exiting the library system. Goodbye!")
        time.sleep(5)
        break
    else:
        print("Invalid choice. Please select a valid option.")


