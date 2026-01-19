def Addition (n1, n2):
    return n1 + n2
def Subtraction (n1, n2):
    return n1 - n2
def multiplication (n1, n2):
    return n1 * n2
def Division (n1, n2):
    return n1 // n2

while True:
    print('''======\033[92m\033[1mSimple Calculator\033[0m======
                [1] Addition
                [2] Subtraction
                [3] Multiplication
                [4] Division
                [5] Exit''')
    print()
    opt = int(input('Select Option: '))
    if opt == 1:
        n1 = int(input("Enter First Number: "))
        n2 = int(input("Enter Second Number: "))
        result = Addition (n1, n2)
        print('=======', "Result: ", result, '=======' )
        print()
    elif opt ==2:
        n1 = int(input("Enter First Number: "))
        n2 = int(input("Enter Second Number: "))
        result = Subtraction(n1, n2)
        print('=======', "Result: ", result, '=======' )
        print()
    elif opt == 3:
        n1 = int(input("Enter First Number: "))
        n2 = int(input("Enter Second Number: "))
        result = multiplication(n1, n2)
        print('=======', "Result: ", result, '=======' )
        print()
    elif opt == 4:
        n1 = int(input("Enter First Number: "))
        n2 = int(input("Enter Second Number: "))
        result = Division(n1, n2)
        print('=======', "Result: ", result, '=======' )
        print()
    elif opt == 5:
        break
    else:
        print('Wrong Input. Try Again!')