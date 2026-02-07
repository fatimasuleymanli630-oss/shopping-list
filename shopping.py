shopping_list = []

def show_list():
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("Shopping list:")
        for item in shopping_list:
            print(f"- {item}")

def add_item():
    item = input("Enter an item: ")
    shopping_list.append(item)
    print(f"{item} added!")

def remove_item():
    item = input("Enter an item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed!")
    else:
        print(f"{item} not found.")

while True:
    action = input("Choose: show / add / remove / quit: ").lower()
    if action == "show":
        show_list()
    elif action == "add":
        add_item()
    elif action == "remove":
        remove_item()
    elif action == "quit":
        break
    else:
        print("Invalid option.")
