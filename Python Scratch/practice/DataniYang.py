name = input("Enter Name: ")
print()
Select = 1
print(f"Hi! {name} What do u want to know:")
while Select != 0:
    Select = int(input('''Know the symptoms:
    [1] Gonorrhea
    [2] Human Papillomavirus'
    [3] Chlamydia
    [0] Exit
    Hmmmm? '''))
    if Select == 1:
        print(''' symptoms:
        1. Happy
        2. Sad''')
    elif Select == 2:
        print(''' symptoms:
        1. Crying
            2. Jumping''')
    elif Select == 3:
        print(''' symptoms:
        1. Punching
        2. Dancing''')
    elif Select == 0:
        break
    else:
        "Wrong Input! Again."

