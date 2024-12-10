from calculator import SimpleCalculator


while True:
    num1=eval(input("Enter First Number:"))
    num2=eval(input("Enter Second Number:"))
    user_input=input("Enter operator: ")
    Calc=SimpleCalculator(num1,num2)
    if user_input=="+":
        print(Calc.add())
    elif user_input=="-":
        print(Calc.subtract())
    elif user_input=="/":
        print(Calc.divide())
    elif user_input=="0":
        print("Goodbye ! see you again")
        break
    else:
        print("You have not typed in a valid operation")
