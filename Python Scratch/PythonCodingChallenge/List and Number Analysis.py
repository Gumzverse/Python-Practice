# Objective:
# Create a Python program that analyzes a list of numbers
# and reports basic statistics.

# Task Requirements:
# 1. Ask the user to input 10 integers.
# 2. Store the numbers in a list.
# 3. Compute and display the following:
#    - The largest number
#    - The smallest number
#    - The average (mean) of the numbers
#    - The number of even values
#    - The number of odd values

# Rules:
# - Use loops (do not use built-in functions like max() or min()).
# - Use only basic Python concepts:
#   * variables
#   * lists
#   * for loop
#   * if-else
# - Output must be clear and labeled.


list = [0] * 10                 #Create a list and can store 10 numbers. 0 is a placeholder or temporary value.

for i in range(10):
    list [i] = int(input(f"Enter number {i+1}: "))

largest = list[0]
smallest = list[0]
sum = 0
evenCount = 0
oddCount = 0

for num in list:
    sum += num

    if num > largest:
        largest = num
    
    if num < smallest:
        smallest = num
    
    if num % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1

average = sum / len(list)

print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
print(f"Average: {average}")
print(f"Even Numbers: {evenCount}")
print(f"Odd Numbers: {oddCount}")



