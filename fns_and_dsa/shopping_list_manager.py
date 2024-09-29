shopping_list = []



def display_menu():
    print("\nshopping list manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")


def add_item():
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"'{item}' has been added to your shopping list.")


def remove_item():
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from your shopping list.")
    else:
        print(f"'{item}' is not in your shopping list.")

def view_list():
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("\n current shopping list:")
        for item in shopping_list:
            print(f"- {item}")

def main():
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            pass
        elif choice == '2':
            # Prompt for and remove an item
            pass
        elif choice == '3':
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()