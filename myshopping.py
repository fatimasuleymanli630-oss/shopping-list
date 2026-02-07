shopping_list = []

def show_list():
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("Your shopping list:")
        total = 0
        for item in shopping_list:
            name, price = item
            total += price
            print(f"- {name}: ${price:.2f}")
        print(f"Total: ${total:.2f}")

def add_item():
    name = input("Enter the item name: ")
    while True:
        try:
            price = float(input(f"Enter the price of {name}: $"))
            break
        except ValueError:
            print("Please enter a valid number.")
    shopping_list.append((name, price))
    print(f"{name} added with price ${price:.2f}!")

def remove_item():
    name = input("Enter the item name to remove: ")
    for item in shopping_list:
        if item[0] == name:
            shopping_list.remove(item)
            print(f"{name} removed!")
            return
    print(f"{name} not found in your list.")

while True:
    print("\nOptions: show / add / remove / quit")
    choice = input("Choose an option: ").lower()
    if choice == "show":
        show_list()
    elif choice == "add":
        add_item()
    elif choice == "remove":
        remove_item()
    elif choice == "quit":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
