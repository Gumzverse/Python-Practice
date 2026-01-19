ctr = 5
while ctr >= 1:
    num = int(input('Input any 3-digit number: '))
    if num < 1000 and num > 99:
        new = int(str(num)[0]) + int(str(num)[1]) + int(str(num)[2])
        print(new)
        ctr -= 1
    else:
        print("Try Again")
        continue


ctr = 5
while ctr >= 1:
    num = int(input('Input any 3-digit number: '))
    if num < 1000 and num > 99:
        digit1 = int(str(num)[0])
        digit2 = int(str(num)[1])
        digit3 = int(str(num)[2])
        new = digit1 + digit2 + digit3
        print(new)
        ctr -= 1
    else:
        print("Try Again")
        continue