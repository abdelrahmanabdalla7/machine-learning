import numpy as np
import pandas as pd

#initalizing the data
data= pd.DataFrame(columns=["Name","Age","Gender","Email"])

#function to enter multiple data
def enter_data():
    while True:
        global data
        name = input("Enter the name: ")
        age = int(input("Enter the age: "))
        gender = input("Enter the gender: ")
        email = input("Enter the email: ")
        new_row = {"Name":name,"Age":age,"Gender":gender,"Email":email}
        data = data._append(new_row, ignore_index=True)
        cont= input("Do you want to add another row? (yes/no): ")
        if cont.lower() != "yes":
            break

#viewing data
def view_data():
    print(f"current data:\n{data}")

#function to add new row
def add_row():
    global data
    while True:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")
        email = input("Enter Email: ")
        new_row = {"Name": name, "Age": age, "Gender": gender, "Email": email}
        data = pd.concat([data, pd.DataFrame([new_row])], ignore_index=True)
        cont = input("Do you want to add another row? (yes/no): ").lower()
        if cont != "yes":
            break

#function to edit an existing row

def edit_row():
    global data
    view_data()
    id=int(input("Enter the id of the row to edit: "))
    new_name=input("Enter the new name: ")
    new_age=int(input("Enter the new age: "))
    new_gender=input("Enter the new gender: ")
    new_email=input("Enter the new email: ")
    data.loc[id] = {"Name":new_name,"Age":new_age,"Gender":new_gender,"Email":new_email}
    print("Row edited successfully!")
    view_data()

#function to delete a row
def delete_row():
    global data
    view_data()
    id=int(input("Enter the id of the row to delete: "))
    data.drop(id, inplace=True)
    print("Row deleted successfully!")
    view_data()

#Function to analysis data
def analysis_data():
    print("\nanalysis data\n1- Filter by age\n2- Sort by column")
    choice=int(input("Enter your choice: "))

    if choice==1:
        min_age= int(input("Enter the minimum age: "))
        max_age= int(input("Enter the maximum age: "))
        filtered_data = data[(data['Age'] >= min_age) & (data['Age'] <= max_age)]
        print(filtered_data)
    
    elif choice == 2:
        column = input("Enter the column to sort by (Name, Age, Gender, Email): ")
        if column in data.columns:
            sorted_data = data.sort_values(by=column)
            print("\nSorted Data:\n", sorted_data)
        else:
            print("Invalid column name!")
    
    else:
        print("Invalid choice")

#Save data to csv file
def save_data():
    data.to_csv("User_DAta_Mangement",index= False)
    print("Data saved successfully!")


while True:
    print("User Data Mangement System")
    print("1- Enter Data")
    print("2- view Data")
    print("3- Add a new Row")
    print("4- Edit a Row")
    print("5- Delete a Row")
    print("6- Analyze Data")
    print("7- Save Data to CSV")
    print("8- Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enter_data()
    elif choice == 2:
        view_data()
    elif choice == 3:
        add_row()
    elif choice == 4:
        edit_row()
    elif choice == 5:
        delete_row()
    elif choice == 6:
        analysis_data()
    elif choice == 7:
        save_data()
    else:
        print("Exiting the program")
        break
    
