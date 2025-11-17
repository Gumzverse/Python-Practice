# Show program title
print('''       Solve for your \33[92mSimple Interest \33[0m''')

# Ask user what type of simple interest they want
print('''       Select Kind Of Simple Interest:
            [1] By Year
            [2] By Days''')

select_button = int(input('      Select: '))

# -------------------------------
# OPTION 1: SIMPLE INTEREST BY YEAR
# -------------------------------
if select_button == 1:
    principle = int(input('     Amount to Borrow: '))   # Money borrowed
    rate = int(input('     Rate of Interest(in Percent): '))  # Interest rate
    year = int(input('     Years to Pay: '))           # Time in years

    rate = rate * 0.01                                 # Convert percent to decimal
    interest = principle * rate * year                 # Simple Interest formula
    A = interest + principle                           # Total amount to pay

# -------------------------------
# OPTION 2: SIMPLE INTEREST BY DAYS
# -------------------------------
elif select_button == 2:
    print('''       Select Kind of Year:
            [1] Ordinary Simple Interest       # uses 360 days
            [2] Exact (Not Leap Year)          # uses 365 days
            [3] Exact (Leap Year)              # uses 366 days''')

    day_type = int(input('       Select: '))

    # Check if user selects a valid option
    if day_type in [1, 2, 3]:
        principle = int(input('     Amount to Borrow: '))     # Money borrowed
        rate = int(input('     Rate of Interest(in Percent): '))  # Interest percent
        days = int(input('     Days To Pay: '))               # Time in days

        rate = rate * 0.01                                    # Convert percent to decimal

        # Change days based on year type
        if day_type == 1:
            days = days / 360
        elif day_type == 2:
            days = days / 365
        elif day_type == 3:
            days = days / 366

        interest = principle * rate * days                    # Simple Interest formula
        A = interest + principle                               # Total amount to pay

    else:
        print("   Invalid Input (Try Again)")                  # Wrong selection
        exit()

# -------------------------------
# INVALID MAIN CHOICE
# -------------------------------
else:
    print("   Invalid Input ")
    exit()

# -------------------------------
# DISPLAY RESULTS
# -------------------------------
print()
print(f"      Interest of your Loan is {interest:.2f}")   # Show final interest
print(f"      Maturity Value is {A:.2f}")                 # Show total amount
