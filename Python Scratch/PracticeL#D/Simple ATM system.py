pin = 1234
pen = int(input("               \033[92mEnter PIN: \033[m"))
balance = 1000
while True:
    if pen != pin:
        print("Kabaw")
        break
    else:
        print('             \033[92m\033[1m---------Access Granted---------\033[0m')

    print('''                      ----------Menu---------
                    [1] Deposit
                    [2] Withdraw
                    [3] Inquire''')
    menu = str(input('              Select Menu: '))
    if menu in '1':
        depo = float(input('             Enter Amount: '))
        new_bal = balance + depo
        print(f"             \033[92m\033[1mDeposit Successful! Your new balance is {new_bal}\033[0m")
        break
    elif menu in '2':
        wit = float(input("               Enter Amount: "))
        if wit > balance:
            print()
            print(f'''               Withdraw Unsuccessful
                `Only Balance Left: {balance}''')
            break
        else:
                new_bal = balance - wit
                print(f"             \033[92m\033[1mWithdraw Successful! Your new balance is {new_bal}\033[0m")
                break
    elif menu in '3':
        print(f"                \033[92mYour Balance is {balance}\033[m")
        break
    else:
        print("           \033[91m\033[1mYour Selected Option is not Supported")
        break

