print("Welcome to the  \033[94mNumber Guessing Game!\033[0m")
print("I'm thinking of a number between 1 and 100.")
import  random
ran1 = (random.randint(1, 100))
list1 = ran1
lives = 5
while True:
 urnum = int(input('1 to 100: '))
 if urnum > list1:
    equ = ' Lower'
    print(equ)
    lives -= 1
 elif urnum< list1:
    equ = 'Higher'
    print (equ)
    lives -= 1
 else:
    print("ur right!!! dahil diyan may kiss ka :>")
    break
 print(f"You only have {lives} lives left.")
 print( )
 if lives == 0:
    print (f'''Bounce na, 'ala ka na buhay. Ang Sagot ay \033[92m{list1}\033[0m''')
    break