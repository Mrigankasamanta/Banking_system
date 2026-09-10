def login():
    with open("account.txt", "r") as f:
        f.seek(0)
        data = f.read()
        accounts = data.splitlines()
    existing_account_nos = []
    pin_match = []
    login_details = []
    for acc in accounts:
        if "Account Number" in acc:
            acc_no = acc.split(":")
            existing_account_no = acc_no[1].replace(" ","")
            existing_account_nos.append(existing_account_no)
        
        if "pin" in acc:
            pin_no = acc.split(":")
            pin_m = pin_no[1].replace(" ","").replace("]","")
            pin_match.append(pin_m)

    for i in range(0,len(existing_account_nos)):
        login_details.append((existing_account_nos[i], pin_match[i]))

    print(existing_account_nos)
    print(pin_match)
    print(login_details)

    # while True:
    #     account_no = input("Enter your account number : ")
    #     if(len(account_no) == 10 and account_no.isdigit()):
    #         break
    #     else:
    #         print("Invalid entry! Account number must be 10 digit. please enter a valid account number...")
         
    # while True:
    #     pin = input("Set your 6 digit security pin : ")
    #     if(len(pin) == 6 and pin.isdigit()):
    #         break
    #     else:
    #         print("Invalid PIN! Please enter valid PIN...")

    # print("account no : ", existing_account_nos)
    # print("entered account no : ",account_no)
    # print("pin list : ",pin_match)
    # print("entered pin : ",pin)

    # if(account_no in existing_account_nos and pin in pin_match):
    #     print("Login Successful! 😊")
    # else:
    #     print("Sorry ligin faild!🙏 This account is not exist in this bank!😔")