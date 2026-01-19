print("*****Rectangle*****")
length = float(input("Enter Length: "))
width = float(input("Enter Width: "))
arear = length * width
perr = 2*length + 2 *width
print ("Area: ", arear)
print ("Perimeter: ", perr)

print("*****Square*****")
Side = float(input("Enter Length: "))
pers = Side * 4
areas = Side * Side
print('Area: ', areas)
print('Perimeter: ', pers)

print("*****Right Triangle*****")
a1 = float(input("Enter Side A/Height: "))
b2 = float(input("Enter Side B/ Base: "))
c3 =float(input("Enter Side C/Hypotenuse: "))
pert = a1 + b2 + c3
areat = 1/2 * b2 * a1
print('Perimeter: ', pert)
print('Area: ', areat)

print("*****Circle*****")
radius = float(input("Enter Radius: "))
diamc = 2 * radius
areac = 3.1415 * (radius **2)
circumc = 2 * 3.1415 * radius
print('Diameter: ', diamc)
print('Area: ', areac)
print('Circumference: ', circumc)