# Pag mag rent 1 to 10 days eh 1000 a day sa Class A, 11 up is -200
# Pag mag rent 1 to 10 days eh 500 a day sa Class B, 11 up is -100

print('''               Welcome To Hotel Calc.''')
print('''             What type is your Hotel
                    [A] Type A
                    [B] Type B''')

con = "Y"  # Initialize con to 'Y'

while con.upper() == "Y":  # Check con.upper() for "Y"
    typ = input('What Type: ')
    if typ.upper() != 'A' and typ.upper() != 'B':
        print("             Invalid Input. Please enter 'A' or 'B'.")
        continue

    days = int(input('''                How Many Days You'll Stay: '''))
    if typ.upper() == 'A':
        if days <= 10:
            worth = days * 1000
        else:
            worth = days * 800
    elif typ.upper() == 'B':
        if days <= 10:
            worth = days * 500
        else:
            worth = days * 400

    print(f"                Worth of Stay is {worth}.")
    con = input("             Wish to Continue[Y]Yes or [N]No: ")