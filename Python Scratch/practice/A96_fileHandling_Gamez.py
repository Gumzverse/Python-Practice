input("Enter the name of you file: ")
read = open("numbers.txt","r")
data = read.readlines()
read.close()

evenfile = open("EvenNUmbers.txt", "w")
oddfile = open("OddNumbers.txt", "w")

total_quantity = 0
even_total = 0
odd_total = 0
negatibnum = 0

for line in data:
    line = line.strip()
    if line.lstrip("-").isdigit():
        num = int(line)
        total_quantity += 1
        if num < 0:
            negatibnum += 1
        if num % 2 == 0:
            evenfile.writelines(line + "\n")
            even_total += num
        else:
            oddfile.write(line + "\n")
            odd_total += num

evenfile.close()
oddfile.close()
print(f"\nThe total quantity of numbers in the file is {total_quantity}")
print(f"The sum of even numbers is {even_total}")
print(f"The sum of odd numbers is {odd_total}")
print(f"The number of negative numbers is {negatibnum}")