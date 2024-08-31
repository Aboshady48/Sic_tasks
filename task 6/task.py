import json # may not be required as per storing method

#Dictionary
with open("login_data.txt", "r") as login_file:
    try:
        users = json.load(login_file)
    except:
        users = {}
        
#Start Menu:Ask if user exists or create new user
def Display_login():
    status =input("Are you a registered user? (Yes/No)? Press q to quit: ")
    if status == "Yes":
        Old_User()
    elif status == "No":
        New_User()
    elif status =="q"or"Q":
        print("see u later")
#Creates New User
def New_User():
    Create_Login =input("Create login name: ")
    if Create_Login in users:
        print ("Login name already exist!")
    else:
        Create_Password =input("Create password: ")
        users[Create_Login] = Create_Password
        print("New User created!")     
#Login if old user
def Old_User():
    login =input("Enter login name: ")
    Password =input("Enter password: ")

    if login in users and users[login] == Password:
        print("Login successful!")
    else:
        print("User doesn't exist or wrong password!")

#currency converter
value = float(input())
in_curr = input()
out_curr = input() 

dict = {'USD': 49.27, 'EUR':  53.6936, 'GBP': 62.5983}

def currency_converter (value,in_curr,out_curr):
    return((dict[in_curr] / dict[out_curr]) * value)

currency_converter()
