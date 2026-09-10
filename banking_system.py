from random import randint
from datetime import datetime

class account:
    def __init__(self, name, dob, phone, pin, account_type, account_no,gmail, balance = 0):
        self.name = name
        self.dob = dob
        self.phone = phone
        self.pin = pin
        self.account_type = account_type
        self.account_no = account_no
        self.gmail = gmail
        self.balance = balance

    def know_details(self):
        print(f"1. Your Account Balance is : {self.balance}\n2. Name : {self.name}\n3. Date Of Birth : {self.dob}\n4. Phone number : +91 {self.phone}\n5. Account Number : {self.account_no}\n6. Account Type : {self.account_type}\n7. Gmail : {self.gmail}")

    # for debit 
    def debit(self, ammount):
        self.balance -= ammount
        print(f"{ammount} is debited from your accont {self.account_no}")
        print(f"Now your account total balance is {self.get_balance()}")

    # for credit 
    def credit(self, ammount):
        self.balance += ammount
        print(f"{ammount} is credited from your accont {self.account_no}")
        print(f"Now your account total balance is {self.get_balance()}")

    def get_balance(self):
        return self.balance

# All fuction for after login use 
def credit(account_no):
    with open("account.txt", "r") as f:
        f.seek(0)
        data = f.read()
        accounts = data.split("]")
    for i, acc in enumerate(accounts):
        if(account_no in acc):
            name = acc.split("Name :")[1].split("\n")[0].strip()
            dob = acc.split("Date Of Birth :")[1].split("\n")[0].strip()
            phone = acc.split("Phone number :")[1].split("\n")[0].strip()
            account_type = acc.split("Account Type :")[1].split("\n")[0].strip()
            gmail = acc.split("Gmail :")[1].split("\n")[0].strip()
            balance = int(acc.split("Your Account Balance is :")[1].split("\n")[0].strip())
            pin = acc.split("pin :")[1].strip()

            coustomer = account(name, dob, phone, pin, account_type, account_no, gmail, balance)
            ammount = int(input("Enter how many money you want to add your account : "))
            coustomer.credit(ammount)

            new_balance = coustomer.get_balance()
            old_line = f"Your Account Balance is : {balance}"
            new_line = f"Your Account Balance is : {new_balance}"
            acc = acc.replace(old_line,new_line)
            accounts[i] = acc
    data = "]".join(accounts)
    with open ("account.txt", "w") as f:
        f.write(data)
            
def debit(account_no, pin):
    with open("account.txt", "r") as f:
        f.seek(0)
        data = f.read()
        accounts = data.split("]")
    for i, acc in enumerate(accounts):
        if(account_no in acc):
            name = acc.split("Name :")[1].split("\n")[0].strip()
            dob = acc.split("Date Of Birth :")[1].split("\n")[0].strip()
            phone = acc.split("Phone number :")[1].split("\n")[0].strip()
            account_type = acc.split("Account Type :")[1].split("\n")[0].strip()
            gmail = acc.split("Gmail :")[1].split("\n")[0].strip()
            balance = int(acc.split("Your Account Balance is :")[1].split("\n")[0].strip())
            
            coustomer = account(name, dob, phone, pin, account_type, account_no, gmail, balance)
            ammount = int(input("Enter how many money you want to add your account : "))
            coustomer.debit(ammount)

            new_balance = coustomer.get_balance()
            old_line = f"Your Account Balance is : {balance}"
            new_line = f"Your Account Balance is : {new_balance}"
            acc = acc.replace(old_line,new_line)
            accounts[i] = acc
    data = "]".join(accounts)
    with open ("account.txt", "w") as f:
        f.write(data)

def show_balance(account_no):
    with open("account.txt", "r") as f:
        f.seek(0)
        data = f.read()
        accounts = data.split("]")
    for acc in accounts:
        if(account_no in acc):
            print(acc.split("1.")[1].split("\n")[0].strip())

def show_details(account_no):
    with open("account.txt", "r") as f:
        f.seek(0)
        data = f.read()
        accounts = data.split("]")
    for acc in accounts:
        if(account_no in acc):
            print(acc.split("[")[1].split("8.")[0].strip())

# For Dasboard after login 

def dasboard(account_no, pin):
    print("Choose one : ")
    while True:
        print("1. For Credit enter --> 1\n2. For Withdrow Balance enter -- > 2\n3. For Show Balance --> 3\n4. For Transaction History enter --> 4\n5. For Account details enter --> 5\n6. For Change PIN enter --> 6\n7. For Close Account enter --> 7\n8. For Logout enter --> 8\n9. For Home enter --> 0" )
        user_input = int(input("Enter your choice : "))

        if(user_input == 1):
            credit(account_no)
            n = int(input("For exit enter --> 1\t\t For continue enter --> 0\nFor home menu enter --> 2 : "))
            if(n == 1):
                print("Thank you!😊 for using THE YOU-R M BANK 💸 ")
                break
            elif(n == 2):
                home()
                break
            elif(n == 0):
                print("Choose one : ")
                continue

        elif(user_input == 2):
            debit(account_no, pin)
            n = int(input("For exit enter --> 1\t\t For continue enter --> 0\nFor home menu enter --> 2 : "))
            if(n == 1):
                print("Thank you!😊 for using THE YOU-R M BANK 💸 ")
                break
            elif(n == 2):
                home()
                break
            elif(n == 0):
                print("Choose one : ")
                continue

        elif(user_input == 3):
            show_balance(account_no)
            n = int(input("For exit enter --> 1\t\t For continue enter --> 0\nFor home menu enter --> 2 : "))
            if(n == 1):
                print("Thank you!😊 for using THE YOU-R M BANK 💸 ")
                break
            elif(n == 2):
                home()
                break
            elif(n == 0):
                print("Choose one : ")
                continue

        elif(user_input == 4):
            print("Coming soon...")
            print("Pleasse choose again :")

        elif(user_input == 5):
            show_details(account_no)
            n = int(input("For exit enter --> 1\t\t For continue enter --> 0\nFor home menu enter --> 2 : "))
            if(n == 1):
                print("Thank you!😊 for using THE YOU-R M BANK 💸 ")
                break
            elif(n == 2):
                home()
                break
            elif(n == 0):
                print("Choose one : ")
                continue

        elif(user_input == 6):
            print("Coming soon...")
            print("Pleasse choose again :")

        elif(user_input == 7):
            print("Coming soon...")
            print("Pleasse choose again :")

        elif(user_input == 8):
            print("Thank you!😊 for using THE YOU-R M BANK 💸 ")
            break

        elif(user_input == 0):
            home()
            break

        else:
            print("Invalid Entry! Please enter a valid number...")
            print("Pleasse choose again :")

        
# for account creation 
def create_account():
    while True:
        name = input("Enter your full name : ")
        if(name.replace(" ","").isalpha()):
            break
        else:
            print("Invalid Name! Please enter valid name...")

    while True:
        dob = input("Enter your date of birth (DD-MM-YYYY) : ")
        try:
            datetime.strptime(dob, "%d-%m-%Y")
            break
        except Exception as e:
            print("Invalid date! Please enter a valid date in 'DD-MM-YYYY' format...")

    while True:
        phone = input("Enter your phone no : +91 ")
        if(len(phone) == 10 and phone.isdigit()):
            break
        print("Invalid phone number! Please enter valid phone number(must be 10 digit)...")

    while True:
        account_type = input("Choose your account type : \n         Enter '1' for Savings Account\n         Enter '2' for Current Account\n         Enter '3' for Salary Account\nEnter your choice : ")
        if (account_type == "1"):
            account_type = "Saving Account"
            break
        elif(account_type == "2"):
            account_type = "Current Account"
            break
        elif(account_type == "3"):
            account_type = "Salary Account"
            break
        else:
            print("Invalid Entry! try again...")
            continue

    while True:
        pin = input("Set your 6 digit security pin : ")
        if(len(pin) == 6 and pin.isdigit()):
            break
        else:
            print("Invalid PIN! Please enter valid PIN...")

    while True:
        gmail = input("Enter your email id (if not present then skip this) : ")
        if(gmail == ""):
            gmail = "Not available"
            break
        elif("@" in gmail):
            break
        else:
            print("Invalid Entry! Enter a valid mail id...")

    while True:
        balance = input("If you want to credit some balance then enter the ammount(if not then skip it) : ")
        if(balance == ""):
            balance = 0
            break
        elif(balance.isdigit()):
            balance = int(balance)
            break
        print("Invalid balance! Please enter valid ammount...")

    with open("account.txt", "r") as f:
        f.seek(0)
        data = f.read()
        lines = data.splitlines()
    existing_account_nos = []
    for line in lines:
        if "Account Number" in line:
            acc_no = line.split(":")
            existing_account_no = acc_no[1].replace(" ","")
            existing_account_nos.append(existing_account_no)

    while True:
        account_no = str(randint(1000000000,9999999999))
        if(account_no in existing_account_nos):
            continue
        else:
            break

    coustomer = account(name, dob, phone, pin, account_type, account_no, gmail, balance)
    with open("account.txt", "a") as f:
        f.write(f"[1. Your Account Balance is : {coustomer.balance}\n2. Name : {coustomer.name}\n3. Date Of Birth : {coustomer.dob}\n4. Phone number : +91 {coustomer.phone}\n5. Account Number : {coustomer.account_no}\n6. Account Type : {coustomer.account_type}\n7. Gmail : {coustomer.gmail}\n8. pin : {coustomer.pin}]\n")
        print("Congratulation!🥳 You successfully created your account 🤗")

    n = int(input("1. for login enter --> 1\n2. for Exit enter --> 0 : "))
    while True:
        if(n == 1):
            print("Login Successful! 😊")
            dasboard(account_no, pin)
        elif(n == 0):
            print("Thank You! 😊 For creating account.🙏")
            break
        else:
            print("Invalid Entry! Enter valid number...")

        

def login():
    with open("account.txt", "r") as f:
        f.seek(0)
        data = f.read()
        accounts = data.split("]")
    login_details = []
    for acc in accounts:
        if "Account Number" in acc and "pin" in acc:
            acc_no = acc.split("Account Number :")[1].split("\n")[0].strip()
            pin = acc.split("pin :")[1].strip()
            login_details.append((acc_no,pin))
        
    while True:
        account_no = input("Enter your account number : ")
        if(len(account_no) == 10 and account_no.isdigit()):
            break
        else:
            print("Invalid entry! Account number must be 10 digit. please enter a valid account number...")
         
    while True:
        pin = input("Set your 6 digit security pin : ")
        if(len(pin) == 6 and pin.isdigit()):
            break
        else:
            print("Invalid PIN! Please enter valid PIN...")

    if((account_no,pin) in login_details):
        print("Login Successful! 😊")
        dasboard(account_no,pin)
    else:
        print("Sorry ligin faild!🙏 This account is not exist in this bank!😔")
        home()


# Home page 

def home():
    while True:
        print("Choose one : ")
        print("1. For create account enter --> 1\n2. For credit enter -- > 2\n3. For Login(for other work) --> 3\n4. Exit enter --> 4" )
        choice = int(input("Enter your choice : "))
        if(choice == 1):
            create_account()
            break
        elif(choice == 2):
            with open("account.txt", "r") as f:
                f.seek(0)
                data = f.read()
                accounts = data.split("]")
            for i in range(1,4):
                a = input("Enter account number : ")
                for acc in accounts:
                    if a in acc:
                        credit(a)
                        break
                else:
                    print("This account nunber is not exist in this bank. Please enter valid account number...")
                    continue
                break
                
        elif(choice == 3):
            login()
            break
        elif(choice == 4):
            break
        else:
            print("Invalid entry! Try again...")

print("         🏦 💵 WELCOME TO THE YOU-R M BANK 💸 🤑 ")
home()








