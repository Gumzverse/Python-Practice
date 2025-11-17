def full_name (first, last):
    print("Hello my Master")
    print(f"Welcome Back to Baggao, Mr.{first}")
    print(f'Son of {last}')

print(full_name("Ian", "Gamez"))

print(full_name("Alfred", "Ramz"))

def sum (x, y):
     ze  =x + y
     return ze

sum(20,50)

ze = sum(12,32)
print(ze)

import array as MYarray
grade = MYarray.array('i', [0] * 5)

def search(arr, value):
    for x in range(len(arr)):
        if arr[x] == value:
            print("found")
            break
    else:
        print("not found")


print("my grade: ")
for x in range(len(grade)):
    grade[x] = int(input())

findd = int(input("enter: "))
search(grade, findd)
