#
"""
- Asks for the user's name and birth year
- Calculates their age in 2025

"""

# Welcome the user and get their name
name = input("What is your name? ").strip().title()  
print(f"Hi {name}!")
print()  #

# Ask for birth year and convert to integer
birth_year = input("Birth Year? ").strip()
print()

# Calculate age based on the year 2025 (update if you reuse this later!)
age = 2025 - int(birth_year)

# Display the calculated age
print(f"You are {age} years old this year.")
print()

if age >= 18:
    print("Agbaak atuyen! ") 
elif age < 17:
    print("Mayat pay atuy agasawa! ") 

print()
response = input(f"Kayat mo agasawan, {name}? ")
print(f"\nAwan pag-asa mon, {name}! ") 

# Optional: Keep the terminal open until user presses Enter (useful on Windows)
input("\nPress Enter to exit...")