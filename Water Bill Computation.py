print ('''          Tuguegarao City Water District
             Tuguegarao City, Cagayan''')
print()
input('     Consumer ID: ')
input('     Consumer Name: ')
wc = float(input('     Water consumption: '))
print()
print ('''      Account Type: 
        [R]Residential
        [C]Commercial
        [I]Industrial''')
typeer = input('        Select Type: ')

if typeer in ('R', 'r'):
    if wc <= 30:
      total = wc * 20
    else:
     total = (30 * 20) + ((wc - 30) * 25)
elif typeer in ('C', 'c'):
    if wc <= 50:
        total = wc * 30
    else:
        total = (50 * 20) + ((wc - 50)* 35)
elif typeer in ('I','i'):
    if wc <= 100:
         total= wc * 50
    else:
        total = (100*50)+ ((wc - 100)* 60)
else:
    print()
    print('     \033[31mInvalid Account Type\033[1m')
    total = 'N/A'
print()
print(f"        \033[0mPAY THIS: \033[92m{total}")