#weight_lbs = input( ' Weight (lbs) : ')
#weight_kg = int(weight_lbs) * 0.45
#print (weight_kg)


print('Temperature Calculator')
print()
temp_cel = input('Temperature (Celsius to Fahrenheit): ')
temp_f = int(temp_cel) * 1.8 + 32
print(temp_f)
print()
temp_f = float(input('Temperature (Fahrenheit to Celsius): '))
temp_cel = (temp_f - 32) * 5/9
print(temp_cel)