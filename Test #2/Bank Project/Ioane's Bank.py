#creating a list for all the users where we store dicts of users:
users = []


#creating a function wich will ask user to enter their name,password, & starter balance and storeing them in a dict while registering:
def create_account():
    name = input("Please enter your Name: ")
    password = input("Please enter your Password: ")
    balance = float(input("Please enter your Starting Balance: "))

    account = {
        "name": name,
        "password": password,
        "balance": balance,
    }

    users.append(account)
    print("Succesfully Registered!")





#creating a function for withdraw or deposit:
def transaction():
#asking an user for their info:
    name = input("Enter your Name: ")
    password = input("Enter your Password: ")
    amount = float(input("Enter transaction amount (-withdraw +deposit): "))

#checking if users inputed info matches information in database:
    for i in users:
        if i["name"] == name and i["password"] == password:
            i["balance"] += amount
            print("Transaction Succesfull")
            print("Updated Balance =", i["balance"])
        else:
#printing if user does not match or if password is incorrect:
            print("Failed to make a Transaction")





#creating an function to update account info
def update_account():
#checking for users information witch has to be updated
    name = input("Please enter your Name: ")
    password = input("Please enter your Password: ")

#if user info matches information in database we ask them for new name and update it in database
    for i in users:
        if i["name"] == name and i["password"] == password:
            updated_name = input("Enter your new username: ")
            if updated_name:
                i["name"] == updated_name
            print("Succesfully Updated Account Information!")

        else:
#printing if user does not match or if password is incorrect:           
            print("Failed To Update Information!")





#creating a function to view all the users:
def view_costumers():
    for i in users:
        print("Account Owner:", i["name"], "Balance:", i["balance"])





def delete():
#checking if info is correct to delete an account:
    name = input("Please enter your Name: ")
    password = input("Please enter your Password: ")

    for i in users:
        if i["name"] == name and i["password"] == password:
            users.remove(i)
            print("Account deleted succesfully!")
        else:
            print("Account not found!")





#creating a main function were user will be able to choose his next step to call a function(1-5)!
def bank():
    while True:
        print("\n------Welcome to Ioane's Bank!------")
        print("Create Account (1)")
        print("Perform Transaction (2)")
        print("Update Account Info (3)")
        print("View Costumers List (4)")
        print("Delete an Account (5)")
        print("Exit (6)")

        next_step = input("Enter your choice: ")
        if next_step == "1":
            create_account()
        elif next_step == "2":
            transaction()
        elif next_step == "3":
            update_account()
        elif next_step == "4":
            view_costumers()
        elif next_step == "5":
            delete()
        elif next_step == "6":
            print("Goodbye! :(")
            break
        else:
            print("Wrong choice, Try again!")

bank()