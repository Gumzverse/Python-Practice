# Ask for user's name
name = input("Enter Name: ")
print()

# Variable used for the loop
Select = 1

print(f"Hi {name}! What do you want to know?")

# Start menu loop
while Select != 0:
    # Main menu
    Select = int(input('''Choose an illness to see its symptoms and treatments:
    [1] Gonorrhea
    [2] Human Papillomavirus (HPV)
    [3] Chlamydia
    [4] Syphilis
    [5] Genital Herpes
    [6] Trichomoniasis
    [7] HIV/AIDS
    [0] Exit
    Your choice: '''))

    # Gonorrhea
    if Select == 1:
        print('''\n=== GONORRHEA ===
Symptoms:
    • Painful urination
    • Yellow/green discharge
    • Pelvic pain

Treatment:
    • Antibiotics (doctor-prescribed)
Treatable?
    ✔ Yes, completely treatable if diagnosed early.
''')

    # HPV
    elif Select == 2:
        print('''\n=== HUMAN PAPILLOMAVIRUS (HPV) ===
Symptoms:
    • Genital warts
    • Sometimes no symptoms at all

Treatment:
    • Warts can be removed (cream/laser)
    • No cure for the virus itself, but body often clears it naturally
Treatable?
    ➖ Virus itself not curable, but manageable.
''')

    # Chlamydia
    elif Select == 3:
        print('''\n=== CHLAMYDIA ===
Symptoms:
    • Painful urination
    • Lower abdominal pain
    • Abnormal discharge

Treatment:
    • Antibiotics from a doctor
Treatable?
    ✔ Yes, fully treatable.
''')

    # Syphilis
    elif Select == 4:
        print('''\n=== SYPHILIS ===
Symptoms (depends on stage):
    • Painless sore
    • Rash on hands/feet
    • Hair loss
    • Fever

Treatment:
    • Penicillin injection (doctor)
Treatable?
    ✔ Yes, treatable in early stages.
''')

    # Genital Herpes
    elif Select == 5:
        print('''\n=== GENITAL HERPES ===
Symptoms:
    • Painful blisters
    • Burning when urinating
    • Itching or tingling

Treatment:
    • Antiviral medication (Acyclovir)
Treatable?
    ➖ Not curable, but symptoms manageable.
''')

    # Trichomoniasis
    elif Select == 6:
        print('''\n=== TRICHOMONIASIS ===
Symptoms:
    • Itching
    • Fishy-smelling discharge
    • Pain during urination

Treatment:
    • Oral antibiotics (Metronidazole)
Treatable?
    ✔ Yes, fully treatable.
''')

    # HIV/AIDS
    elif Select == 7:
        print('''\n=== HIV/AIDS ===
Symptoms:
    • Fever
    • Fatigue
    • Weight loss
    • Weak immune system

Treatment:
    • Antiretroviral therapy (ART)
Treatable?
    ➖ Not curable, but treatable and manageable for life.
''')

    # Exit
    elif Select == 0:
        print("\nExiting... Stay informed and stay safe!")
        break

    # Wrong input
    else:
        print("\nInvalid input! Try again.\n")
