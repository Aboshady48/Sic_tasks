import getpass
import json
import os
import string
import uuid
import hashlib
import base64
try:
    from cryptography.fernet import Fernet
except ImportError:
    print("The cryptography library is not installed. Installing it now...")
    os.system("pip install cryptography")
    print("--------------------------------------------------------------------------")
    print("Installation complete.")
    print("--------------------------------------------------------------------------")
    from cryptography.fernet import Fernet  #1 Data Encryption not Password Encryption
except Exception as e:
    print(f"An error occurred: {e}")


EXCHANGE_RATES_FILE = "exchange_rates.json" #2 Text file not JSON file
ACCOUNTS_FILE = "accounts.json" 

def generate_salt():
    return os.urandom(16)

def hash_password(password, salt):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode() + salt)
    return encrypted_password, key #3 #security Risk 

def verify_password(stored_password, input_password, salt, key):
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(stored_password)
    if decrypted_password == (input_password.encode() + salt):
        return True
    else:
        return False
    
def load_exchange_rates():
    if os.path.exists(EXCHANGE_RATES_FILE):
        with open(EXCHANGE_RATES_FILE, "r") as file:
            return json.load(file)
    else:
        return {}

def add_exchange_rate(currency, rate):
    exchange_rates = load_exchange_rates()
    exchange_rates[currency] = rate
    save_exchange_rates(exchange_rates)

def save_exchange_rates(exchange_rates):
    with open(EXCHANGE_RATES_FILE, "w") as file:
        json.dump(exchange_rates, file)

exchange_rates = { 
    "EGP": 1,
    "USD": 0.02,
    "EUR": 0.017,
    "GBP": 0.015,
    "JPY": 0.008,
    "CAD": 0.012,
    "AUD": 0.010,
    "NZD": 0.013,
    "CHF": 0.011,
    "GBP": 0.015,
    "SGD": 0.011,
    "HKD": 0.007,
    "MYR": 0.003,
    "PHP": 0.006,
    "TWD": 0.003,
    "THB": 0.003,
    "VND": 0.00008,
    "KRW": 0.00009,
    "CNY": 0.007,
    "INR": 0.0008,
    "IDR": 0.00007,
    "TRY": 0.0006,
    "BRL": 0.0005,
    "MXN": 0.0006,
    "ZAR": 0.0008,
    "CAD": 0.012,
    "CLP": 0.0006,
    "COP": 0.0003,
    "PEN": 0.0004,
    "UYU": 0.0004,
    "ARS": 0.0003,
    "BOB": 0.0005,
    "JPY": 0.0008,
    "CNY": 0.007,
    "INR": 0.0008,
    "IDR": 0.00007,
    "TRY": 0.0006,
    "BRL": 0.0005,
    "MXN": 0.0006,
    "ZAR": 0.0008,
    "CAD": 0.012,
    "CLP": 0.0006,
}

for currency, rate in exchange_rates.items():
    add_exchange_rate(currency, rate)

def exchange_coin(coin, balance):
    exchange_rates = load_exchange_rates()

    if coin in exchange_rates:
        rate = exchange_rates[coin]
        egp_amount = balance / rate
        print(f"Exchanging {balance} {coin} to {egp_amount:.2f} EGP")
        return egp_amount
    else:
        print(f"Unknown coin type: {coin}")
        return 0.0

def load_accounts():
    """
    Function to load user accounts from the JSON file
    """
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, "r") as file:
            return json.load(file)
    else:
        return {}

def save_accounts(accounts):
    """
    Function to save user accounts to the JSON file
    """
    with open(ACCOUNTS_FILE, "w") as file:
        json.dump(accounts, file)

accounts = load_accounts()
def create_account():
    """
    Function to create a new user account
    """
    print("*****************Welcome to sign up page**********************")

    while True:
        username = input("Enter your username: ").lower()
        if username.replace(" ", "") == username:  # Check if there are no spaces
            if username.replace("_", "").replace("-", "").isalnum():  # Check if username only contains letters, numbers, _, and -
                if username:
                    if not username.replace("_", "").replace("-", "").isdigit():  # Check if username is not only digits
                        if username in accounts:
                            print("Username already exists. Please choose a different one.")
                        else:
                            break
                    else:
                        print("Username cannot be only numbers. Please try again.")
                else:
                    print("Username cannot be empty. Please try again.")
            else:
                print("Username can only contain letters, numbers, _, and -. Please try again.")
        else:
            print("Username cannot contain spaces. Please try again.")
    
    while True:
        password = getpass.getpass("Enter your password: ")
        confirm_password = getpass.getpass("Confirm your password: ")
        if password == confirm_password:
            break
        print("Passwords do not match. Please try again.")
    
    if password == confirm_password:
        while True:
            name = input("Enter your name: ")
            if name.replace(" ", "").isalpha():
                break
            else:
                print("Name cannot be empty or contain numbers/special characters. Please try again.")

        phone = input("Enter your phone number: ")
        while not phone or not phone.isdigit() or len(phone) != 11:
            print("Invalid phone number. Please enter a 11-digit number.")
            phone = input("Enter your phone number: ")

        gender = input("Enter your gender (M/F): ").upper()
        while gender not in ['M', 'F']:
            print("Invalid gender. Please enter M for male or F for female.")
            gender = input("Enter your gender (M/F): ").upper()

        while True:
            age = input("Enter your age: ")
            if age.isdigit():
                age = int(age)
                if 18 <= age <= 100:
                    break
                else:
                    print("Invalid age. Please enter a number between 18 and 100.")
            else:
                print("Invalid age. Please enter a number.")

        city = input("Enter your city: ")
        while not all(char.isalpha() or char.isspace() for char in city):
            print("Invalid City. Please try again.")
            city = input("Enter your city: ")
        

        if username not in accounts:
            user_id = hashlib.sha256(str(uuid.uuid4()).encode()).hexdigest()[:8]
            salt = generate_salt()
            hashed_password, key = hash_password(password, salt)
            accounts[username] = {
                "name": name,
                "password": hashed_password.decode(),
                "key": base64.b64encode(key).decode(),  #4
                "salt": base64.b64encode(salt).decode(), #4 save it before decode and decode it when the user enter the password, BUT IT'S JSON FILE SO IT'S A MOST
                "phone": phone,
                "gender": gender,
                "age": age,
                "city": city,
                "id": user_id,
                "balance": 0,
                "transactions": [],
                "transactions_count": 0,
                "withdrawals_count": 0,
                "deposits_count": 0,
            }
            #Transactions cout
            save_accounts(accounts)
            print("Account created successfully!")
            print("Your ID is ", user_id)
        else:
            print("Username already exists. Please try again.")
            create_account()
    else:
        print("Passwords do not match. Please try again.")
        create_account()
def login_account():
    print("**************************Welcome to Login Page************************")
    """
    Function to login to an existing user account
    """
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        login_id = input("Enter your username or ID: ").lower()
        
        try:
            for username, account in accounts.items():
                if login_id == username or login_id == account["id"]:
                    stored_password = account["password"]
                    key = base64.b64decode(account["key"].encode())  
                    salt = base64.b64decode(account["salt"].encode())  
                    myName = account["name"]
                    password = getpass.getpass("Enter your password: ")
                    if verify_password(stored_password, password, salt, key):
                        print("Login successful!")
                        print(f"***********************Welcome back, {myName}!***********************************")
                        account_operations(username)
                    else:
                        print("Invalid password. Please try again.")
                    break
            else:
                print("Invalid username or ID. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        attempts += 1

    print("Maximum login attempts reached. Please try again later.")

def account_operations(username):

    while True:
        print("[0] Deposit")
        print("[1] Withdraw")
        print("[2] Transfer")
        print("[3] Check Balance & Personal info")
        print("[4] Transaction History") #bouns yaret
        print("[5] Logout")
        
        choice = input("Enter your choice: ")
        match choice:
            case "0":
                deposit(username)
            case "1":
                withdraw(username)
            case "2":
                transfer(username)
            case "3":
                personalInfo(username)
            case "4":
                transaction_history(username)
            case "5":
                logout(username)
            case _:  # default case
                print("Invalid choice. Please try again.")

def deposit(username):
    # Implement deposit functionality
    while True:
        user_input = input("Please enter the amount you want to deposit and the currency in this format '100 EGP': ")
        try:
            balance, coin = user_input.split()
            balance = float(balance)
            coin = coin.upper()
            if balance > 0:
                if coin == 'EGP':
                    accounts[username]["balance"] += balance
                    accounts[username]["transactions"].append(f"Deposited {balance} EGP")
                    accounts[username]["transactions_count"] += 1
                    accounts[username]["deposits_count"] += 1
                    save_accounts(accounts)
                    print("Deposit successful!")
                    print(f"Your current balance is: {accounts[username]['balance']} EGP")
                    break
                elif coin in exchange_rates:
                    egp_amount = exchange_coin(coin, balance)
                    accounts[username]["balance"] += egp_amount
                    accounts[username]["transactions"].append(f"Deposited {balance} {coin}")
                    accounts[username]["transactions_count"] += 1
                    accounts[username]["deposits_count"] += 1
                    save_accounts(accounts)
                    print("Deposit successful!")
                    print(f"Your current balance is: {accounts[username]['balance']} EGP")
                    break
                else:
                    print("Invalid currency. Please try again.")
            else:
                print("Invalid deposit amount. Please try again.")
        except ValueError:
            print("Invalid input format. Please try again.")

def withdraw(username):
    while True:
        user_input = input("Please enter the amount you want to withdraw and the currency in this format '1 EGP' : ")
        try:
            balance, coin = user_input.split()
            balance = float(balance)
            coin = coin.upper()
            if balance > 0:
                if coin == 'EGP':
                    if balance <= accounts[username]["balance"]:
                        accounts[username]["balance"] -= balance
                        accounts[username]["transactions"].append(f"Withdrew {balance} EGP")
                        accounts[username]["transactions_count"] += 1
                        accounts[username]["withdrawals_count"] += 1
                        save_accounts(accounts)
                        print("Withdrawal successful!")
                        print(f"Your current balance is: {accounts[username]['balance']} EGP")
                        break
                    else:
                        print("Insufficient balance. Please try again.")
                elif coin in exchange_rates:
                    egp_amount = exchange_coin(coin, balance)
                    if egp_amount <= accounts[username]["balance"]:
                        accounts[username]["balance"] -= egp_amount
                        accounts[username]["transactions"].append(f"Withdrew {balance} {coin}")
                        accounts[username]["transactions_count"] += 1
                        accounts[username]["withdrawals_count"] += 1
                        save_accounts(accounts)
                        print("Withdrawal successful!")
                        print(f"Your current balance is: {accounts[username]['balance']} EGP")
                        break
                    else:
                        print("Insufficient balance. Please try again.")
                else:
                    print("Invalid currency. Please try again.")
            else:
                print("Invalid withdrawal amount. Please try again.")
        except ValueError:
            print("Invalid input format. Please try again.")
           
def get_transfer_amount():
    """Get the transfer amount and currency from the user."""
    while True:
        user_input = input("Please enter the amount you want to transfer and the currency in this format '100 EGP' : ")
        try:
            balance, coin = user_input.split()
            balance = float(balance)
            coin = coin.upper()
            if balance <= 0:
                print("Invalid transfer amount. Please try again.")
                continue
            return balance, coin
        except ValueError:
            print("Invalid input format. Please try again.")

def get_recipient(accounts: dict) -> str:
    """Get the recipient's username or ID from the user."""
    while True:
        recipient_input = input("Please enter the username or ID of the account you want to transfer money to: ").lower()
        for username, account in accounts.items():
            if recipient_input == username or recipient_input == account["id"]:
                recipient_username = username
                return recipient_username  # Return the username, not the input
        print("Invalid recipient username or ID. Please try again.")

def confirm_transfer(accounts, recipient_username):
    """Confirm the transfer with the user."""
    account_info = next((account for account in accounts.values() if account["username"] == recipient_username), None)
    print(f"You are about to transfer money to: {recipient_username}")
    print(f"Account ID: {account_info['id']}")
    print(f"Account Username: {account_info['username']}")
    print(f"Account Name: {account_info['name']}")
    confirm = input("Is this the correct account? (yes/no): ")
    return confirm.lower() == "yes"

def perform_transfer(accounts, username, recipient_username, balance, coin):
    """Perform the transfer."""
    if coin == 'EGP':
        if balance <= accounts[username]["balance"]:
            accounts[username]["balance"] -= balance
            accounts[username]["transactions"].append(f"Transferred {balance} EGP to {recipient_username}")
            accounts[username]["transactions_count"] += 1
            accounts[username]["transfers_count"] += 1
            accounts[recipient_username]["balance"] += balance
            accounts[recipient_username]["transactions"].append(f"Received {balance} EGP from {username}")
            accounts[recipient_username]["transactions_count"] += 1
            accounts[recipient_username]["deposits_count"] += 1
            save_accounts(accounts)
            print("Transfer successful!")
            print(f"Your current balance is: {accounts[username]['balance']:.2f} EGP")
            return True
        else:
            print("Insufficient balance. Please try again.")
            return False
    elif coin in exchange_rates:
        egp_amount = exchange_coin(coin, balance)
        if egp_amount <= accounts[username]["balance"]:
            accounts[username]["balance"] -= egp_amount
            accounts[username]["transactions"].append(f"Transferred {balance} {coin} to {recipient_username}")
            accounts[username]["transactions_count"] += 1
            accounts[username]["transfers_count"] += 1
            accounts[recipient_username]["balance"] += egp_amount
            accounts[recipient_username]["transactions"].append(f"Received {balance} {coin} from {username}")
            accounts[recipient_username]["transactions_count"] += 1
            accounts[recipient_username]["deposits_count"] += 1
            save_accounts(accounts)
            print("Transfer successful!")
            print(f"Your current balance is: {accounts[username]['balance']:.2f} EGP")
            return True
        else:
            print("Insufficient balance. Please try again.")
            return False
    else:
        print("Invalid currency. Please try again.")
        return False
def transfer(username):
    """Initiate a transfer."""
    balance, coin = get_transfer_amount()
    recipient_username = get_recipient(accounts)
    if not confirm_transfer(accounts, recipient_username):
        print("Transfer cancelled.")
        return
    if perform_transfer(accounts, username, recipient_username, balance, coin):
        print("Transfer successful!")
        print(f"Your current balance is: {accounts[username]['balance']:.2f} EGP")
'''
def transfer(username):
    while True:
        user_input = input("Please enter the amount you want to transfer and the currency in this format '100 EGP' : ")
        try:
            balance, coin = user_input.split()
            balance = float(balance)
            coin = coin.upper()
            if balance <= 0:
                print("Invalid transfer amount. Please try again.")
                continue
            recipient_input = input("Please enter the username or ID of the account you want to transfer money to: ").lower()
            recipient = ""
            for account in accounts.values():
                if account["username"].lower() == recipient_input or account["id"] == recipient_input:
                    recipient = account["username"]
                    break
            if recipient is None:
                print("Invalid recipient username or ID. Please try again.")
                continue
            print(f"You are about to transfer money to: {recipient}")
            account_info = next((account for account in accounts.values() if account["username"] == recipient), None)
            if account_info is None:
                print("Invalid recipient username or ID. Please try again.")
                continue
            print(f"Account ID: {account_info['id']}")
            print(f"Account Username: {account_info['username']}")
            print(f"Account Name: {account_info['name']}")
            confirm = input("Is this the correct account? (yes/no): ")
            if confirm.lower()!= "yes":
                print("Transfer cancelled.")
                return
            if coin == 'EGP':
                
            elif coin in exchange_rates:
               )
        except ValueError:
            print("Invalid input format. Please try again.")
'''

def personalInfo(username):
    # Implement check balance functionality
    accounts = load_accounts() #6 It should be check password before showing the info, Sorry :(
    if username in accounts:
        print(f"Name: {accounts[username]['name']}")
        print(f"Phone: {accounts[username]['phone']}")
        print(f"Gender: {accounts[username]['gender']}")
        print(f"Age: {accounts[username]['age']}")
        print(f"City: {accounts[username]['city']}")
        print(f"Current Balance: {accounts[username]['balance']} EGP")
        print(f"Total Transactions: {accounts[username]['transactions_count']}")
        print(f"Total Withdrawals: {accounts[username]['withdrawals_count']}")
        print(f"Total Deposits: {accounts[username]['deposits_count']}")
        print("*************************************************************")
    pass
def transaction_history(username):
    # Implement transaction history functionality
    accounts = load_accounts()
    if username in accounts:
        print("Transaction History:")
        for transaction in accounts[username]['transactions']:
            print(transaction)
        print("*************************************************************")
    else:
        print("Invalid username. Please try again.")
    pass
def logout(username):
    # Implement logout functionality
    print(f"Bye {username}, See You Later")
    print("Logging out...")
    exit()

def main():

    while True:
        print("*****************Welcome to SIC Bank Management System***************")
        print("if you already have an account Enter login")
        print("if you don't have an account Enter register")
        print("if you want to Exit Enter e")

        choice = input("").lower()

        if choice == "register":
            create_account()
        elif choice == "login":
            login_account()
        elif choice == "e":
            print("Thank you for using SIC Bank Management System!")
            break
        else:
            print("Invalid choice. Please try again.")
            break #Continue :(  , 8lta we74a awy, kont h3dlha bs elba4mohandesa nour 2let la , Sorry


if __name__ == "__main__":
    main()