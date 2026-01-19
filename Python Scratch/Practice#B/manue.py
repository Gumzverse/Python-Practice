class Node:
    name = None
    link = None

head = None

def add_booking(new_name):
    global head
    new_node = Node()
    new_node.name = new_name
    new_node.link = None

    if head == None:
        head = new_node

    else:
        current = head
        while current.link != None:
            current = current.link
        current.link = new_node

def booking_summary():
    global head
    if head == None:
        print("Book list is empty.")

    else:
        print("Bookings:")
        current = head
        while current != None:
            print(f"* {current.name}")
            current = current.link

def del_booking(name_to_cut):
    global head
    current = head
    previous = None

    while current != None:
        if current.name == name_to_cut:
            if previous == None:
                head = current.link
            else:
                previous.link = current.link
            print(f"Booking '{name_to_cut}' deleted.")
            return
        previous = current
        current = current.link
    print(f"Booking '{name_to_cut}' not found.")

def start():
    while True:
        print("------Welcome to our Booking System------")
        print("\n1. Add Booking")
        print("2. Delete booking")
        print("3. View Bookings")
        print("4. Exit")

        select = int(input("\nSelect an option: "))

        if select == 1:
            name = input("Enter booking name: ")
            add_booking(name)
        elif select == 2:
            name = input("Enter booking name: ")
            del_booking(name)
        elif select == 3:
            booking_summary()
        elif select == 4:
            print("\nThank you for using our Booking System.")
            print("Have a wonderful day!")
            break
        else:
            print("INVALID OPNTION.")

start()