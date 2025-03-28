accounts = { 
    1001: ["user 1", "14-08-25", "1429", 10000],  
    1002: ["user 2", "29-03-25", "2008", 20000],
    1003: ["user 3", "13-05-25", None, 30000],  
}

print("Welcome!")

while True:
    print("***********************************")
    print("1. Withdrawal")
    print("2. Deposit")
    print("3. PIN Generation")
    print("4. Mini Statement")
    print("5. Exit")
    
    try:
        x = int(input("Enter your option: "))
    except ValueError:
        print("Please enter a valid number!")
        continue
    
    if x == 1:  # Withdrawal
        accno = int(input("Enter account number: "))
        if accno not in accounts:
            print("No user exists with this account number.")
        elif accounts[accno][-2] is None:
            print("Generate a PIN before withdrawal.")
        else:
            pin = input("Enter PIN: ")
            if str(accounts[accno][-2]) != pin:  
                print("Invalid PIN, try again.")
            else:
                amt = int(input("Enter amount to withdraw: "))
                if amt <= accounts[accno][-1]:
                    accounts[accno][-1] -= amt
                    print("Withdrawal successful!")
                else:
                    print("Insufficient funds.")
    
    elif x == 2:  # Deposit
        accno = int(input("Enter account number: "))
        if accno not in accounts:
            print("No user exists with this account number.")
        else:
            amt = int(input("Enter amount to be deposited: "))
            accounts[accno][-1] += amt
            print("Deposit successful!")
    
    elif x == 3:  # PIN Generation
        accno = int(input("Enter account number: "))
        if accno not in accounts:
            print("No user exists with this account number.")
        elif accounts[accno][-2] is not None:
            print("PIN already generated.")
        else:
            pin = input("Enter PIN: ")
            cpin = input("Re-enter PIN: ")
            if pin != cpin:
                print("PIN does not match.")
            else:
                accounts[accno][-2] = pin  
                print("PIN generated successfully!")
    
    elif x == 4:  # Mini Statement
        accno = int(input("Enter account number: "))
        if accno not in accounts:
            print("No user exists with this account number.")
        elif accounts[accno][-2] is None:
            print("Generate a PIN before accessing the mini statement.")
        else:
            pin = input("Enter PIN: ")
            if str(accounts[accno][-2]) != pin:
                print("Invalid PIN, try again.")
            else:
                print(f"Account Number: {accno}")
                print(f"Name: {accounts[accno][0]}")
                print(f"Date of Birth: {accounts[accno][1]}")
                print(f"Balance: {accounts[accno][-1]}")
    
    elif x == 5:  # Exit
        print("Thank you!")
        break
    
    else:
        print("Choose a correct option!")
