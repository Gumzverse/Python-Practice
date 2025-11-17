ident = [1,2,3]
ident1= {1,2,3}
ident2 = (1,2,3)

inventory = {
    "apple": {"price": 45.00, "quantity": 120},
    "banana": {"price": 10.00, "quantity": 150},
    "orange": {"price": 30.00, "quantity": 80},
    "grape": {"price": 1.50, "quantity": 120},
    "watermelon": {"price": 60.00, "quantity": 50},
}

#"pineapple", 65.50, 70)
def add_product(name, price, quantity):
    inventory[name] = {"price": price, "quantity": quantity}
    print(f"{name} added to inventory.")
#"banana", 10.00
def update_price(name, new_price):
    if name in inventory:
        inventory[name]["price"] = new_price
        print(f"Price of {name} updated to {new_price}.")
    else:
        print(f"{name} not found in inventory.")
#x"apple", 120
def update_quantity(name, new_quantity):
    if name in inventory:
        inventory[name]["quantity"] = new_quantity
        print(f"Quantity of {name} updated to {new_quantity}.")
    else:
        print(f"{name} not found in inventory.")

def display_inventory():
    print("Current Inventory:")
    for product, details in inventory.items():
        print(f"Product: {product}, Price: {details['price']}, Quantity: {details['quantity']}")

add_product("pineapple", 65.50, 70)
update_price("banana", 10.00)
update_quantity("apple", 120)
display_inventory()