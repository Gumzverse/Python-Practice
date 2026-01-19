# Initializing score and map
sand = [["[-]" for x in range(5)] for y in range(5)]
score = 0

# checker for treasure
treasures = [["[-]" for a in range(5)] for b in range(5)]
treasures[0][0] = "[1]"
treasures[0][1] = "[2]"
treasures[0][2] = "[3]"
treasures[0][3] = "[4]"
treasures[0][4] = "[5]"

for attempt in range(10, 0,-1):
    print(f"you have {attempt} attempts left")
    print("      0  1  2  3  4")
    for x in range(len(sand)):
        print(f"  {x}  ", end="")
        for y in range(len(sand[0])):
            print(sand[x][y],end="")
        print()
    print("Select Indices: ")
    row = int(input("Select Row: "))
    col = int(input("Select Column: "))

    if treasures[row][col] == "[1]":
        if sand[row][col] == "[-]":
            print("You did some Digging...")
            print("You found treasure! (+1)")
            sand[row][col] = "[1]"
            score += 1
        else:
            print("You already dug this up!")
            sand[row][col] = "[*]"
            treasures[row][col] = "[*]"
    elif treasures[row][col] == "[2]":
        if sand[row][col] == "[-]":
            print("You did some Digging...")
            print("You found treasure! (+2)")
            sand[row][col] = "[2]"
            score += 2
        else:
            print("You already dug this up!")
            sand[row][col] = "[*]"
            treasures[row][col] = "[*]"
    elif treasures[row][col] == "[3]":
        if sand[row][col] == "[-]":
            print("You did some Digging...")
            print("You found treasure! (+3)")
            sand[row][col] = "[3]"
            score += 3
        else:
            print("You already dug this up!")
            sand[row][col] = "[*]"
            treasures[row][col] = "[*]"

    elif treasures[row][col] == "[4]":
        if sand[row][col] == "[-]":
            print("You did some Digging...")
            print("You found treasure! (+4)")
            sand[row][col] = "[4]"
            score += 4
        else:
            print("You already dug this up!")
            sand[row][col] = "[*]"
            treasures[row][col] = "[*]"

    elif treasures[row][col] == "[5]":
        if sand[row][col] == "[-]":
            print("You did some Digging...")
            print("You found treasure! (+5)")
            sand[row][col] = "[5]"
            score += 5
        else:
            print("You already dug this up!")
            sand[row][col] = "[*]"
            treasures[row][col] = "[*]"
    else:
        if sand[row][col] == "[-]":
            print("You did some Digging...")
            print("You found nothing. Try again")
            sand[row][col] = "[*]"
            treasures[row][col] = "[*]"
        else:
            print("You already dug this up!")

    if score == 15:
        break
# Finished Game
if score == 0:
    print("You found nothing! not even one")
    print(f"final score: {score}\n")
elif score < 15:
    print("At least you found some")
    print(f"final score: {score}\n")
elif score == 15:
    print("You Found Everthing!")
    print(f"final score: {score}\n")
print("final map:\n")

#Reveals all treasures
print("      0  1  2  3  4")
for x in range(len(treasures)):
    print(f"  {x}  ", end="")
    for y in range(len(treasures[0])):
        print(sand[x][y],end="")
    print()