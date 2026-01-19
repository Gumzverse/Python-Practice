class Node:
    data =  None
    next = None

head = None

def AddPass ():
    global head
    Name =  input("Enter Name of Passenger: ")
    new_pass = Node()
    new_pass.data = Name
    new_pass.next = head
    head = new_pass
    print("Passenger added. Thank you!")

def CanBook ():
    global head
    if head is None:
        print("No passengers to cancel.")
        return
    Name =  input("Enter Name of Passenger: ")
    if head.data == Name:
        head.next = head
        print(f"Passenger {Name} Removed")
        return
    neww = head
    while neww.next != None:
        if neww.next.data == Name:
            neww.next = neww.next.next
            print(f"Passenger {Name} Removed")
            return
        neww = neww.next
    print("Passenger not found.")
    return

def DisPas ():
    global head
    ctr =1
    if head is None:
        print("No Passengers.")
        return
    print("Passenger List:")
    cur = head
    while cur != None:
        print(f'''{ctr}. ''', cur.data)
        cur = cur.next
        ctr += 1
    print()



while True:
    print('''---------------Flight Booking System---------------
    [1] Add Passenger
    [2] Cancel Booking
    [3] Display Passengers
    [4] Exit
    ----------------------------------------------------''')
    fbs = int(input("Select: "))
    if fbs == 1:
        AddPass ()
    elif fbs == 2:
         CanBook()
    elif fbs == 3:
        DisPas()
    elif  fbs == 4:
        print("Thank You for Using our Flight Booking System")
        break
    else:
        print("Selected Character not Supported. Try Again")
