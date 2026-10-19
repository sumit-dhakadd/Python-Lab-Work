from collections import Counter

# Combine stock from multiple stores
def combine_stores(*stores):
    total_stock = Counter()

    for stock in stores:
        total_stock.update(stock)

    return dict(total_stock)

# Print inventory
def show_stock(data):
    print("\nInventory Details:")
    for name in data:
        print(name, ":", data[name])

# Search for an item
def find_stock(data):
    search = input("\nEnter item name to check: ")

    quantity = data.get(search)
    if quantity is None:
        print("Item not found.")
    else:
        print("Available Quantity:", quantity)

# Store inventories
store1 = {"Pen": 20, "Book": 15, "Pencil": 30}
store2 = {"Pen": 10, "Book": 25, "Eraser": 12}
store3 = {"Pencil": 15, "Eraser": 8}

# Merge all inventories
inventory = combine_stores(store1, store2, store3)
show_stock(inventory)

# Copy inventory and add extra stock
updated_inventory = inventory.copy()
extra_stock = {"Pen": 5, "Marker": 10}

for name, amount in extra_stock.items():
    if name in updated_inventory:
        updated_inventory[name] += amount
    else:
        updated_inventory[name] = amount

print("\nUpdated Inventory:")
show_stock(updated_inventory)

# Check available quantity
find_stock(updated_inventory)
