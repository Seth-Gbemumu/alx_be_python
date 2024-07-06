def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} successfully added to the shopping list.")
        elif choice == '2':
            # Prompt for and remove an item
            item = input ("Enter the item you want to remove from the shopping list: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} successfully removed from the shopping list.")
            else:
                print(f"{item} is not on the shopping list.")
        elif choice == '3':
            # Display the shopping list
            print("Shopping List:")
            for i, item in enumerate(shopping_list, start = 1):
                print(f"{i}. {item}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()