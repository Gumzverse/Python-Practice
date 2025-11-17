row = [[1,2,3],[21,13,14],[8,9,6]]


#Display
for x in row:
    for y in x:
        print(y, end=", ")
print()

def changeallcolumns3ofeachRowto0 ():
        for r in row:
            r[2] = 0
changeallcolumns3ofeachRowto0()
for x in row:
    for y in x:
        print(y, end=", ")
print()