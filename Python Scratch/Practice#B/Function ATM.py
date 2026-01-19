def atm_password(password):
    pas = int(input('Enter password: '))
    if pas == password:
        print('Password Validated Successfully.')
        return True
    else:
        print('Invalid Password.')
        return False

def deposit(balance):
    dp = int(input('Enter amount: '))
    balance += dp
    print(f'Transaction successful.\nAmount Deposited: {dp}\nBalance: {balance}')
    return balance

def withdraw(balance):
    wd = int(input('Enter amount: '))
    if wd > balance:
        print('Insufficient Balance.')
    else:
        balance -= wd
        print(f'Transaction successful.\nAmount Withdrawn: {wd}\nBalance: {balance}')
    return balance

def inquire(balance):
    print(f'Your Balance is: {balance}')
    return balance

def menu():
    balance = 10000
    password = 1234
    if not atm_password(password):
        return
    while True:
        print('\n[1] Deposit\n[2] Withdraw\n[3] Inquire\n[4] Exit')
        option = input('Enter option: ')
        if option == "1":
            balance = deposit(balance)
        elif option == "2":
            balance = withdraw(balance)
        elif option == "3":
            inquire(balance)
        elif option == "4":
            print('Thank you for using the ATM!')
            break
        else:
            print('Invalid option. Please try again.')

menu()