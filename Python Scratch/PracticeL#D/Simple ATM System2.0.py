# ATM Program without functions

# Initial account setup
balance = 10000      # Starting balance
password = 1234      # ATM password

# Ask user for password
entered_password = int(input("Enter password: "))
if entered_password != password:
    print("Invalid Password.")
else:
    print("Password Validated Successfully.")

    # Start main menu loop
    while True:
        print("\n===== ATM MENU =====")
        print("[1] Deposit")
        print("[2] Withdraw")
        print("[3] Inquire Balance")
        print("[4] Exit")
        
        option = input("Enter option: ")

        # Deposit money
        if option == "1":
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            print(f"Transaction successful.\nAmount Deposited: {amount}\nBalance: {balance}")

        # Withdraw money
        elif option == "2":
            amount = int(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient Balance.")
            else:
                balance -= amount
                print(f"Transaction successful.\nAmount Withdrawn: {amount}\nBalance: {balance}")

        # Check balance
        elif option == "3":
            print(f"Your Balance is: {balance}")

        # Exit ATM
        elif option == "4":
            print("Thank you for using the ATM!")
            break

        # Invalid option
        else:
            print("Invalid option. Please try again.")
