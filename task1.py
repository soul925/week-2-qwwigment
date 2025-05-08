# Predefined list of users
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

def create_user():
    try:
        id = int(input("Enter ID: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return
    name = input("Enter name: ")
    email = input("Enter email: ")
    users.append({"id": id, "name": name, "email": email})
    print("User added.")

def read_user():
    try:
        id = int(input("Enter ID to retrieve: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return
    for user in users:
        if user["id"] == id:
            print("User found:", user)
            return
    print("User not found.")

def update_user():
    try:
        id = int(input("Enter ID to update: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return
    for user in users:
        if user["id"] == id:
            user["name"] = input("Enter new name: ")
            user["email"] = input("Enter new email: ")
            print("User updated.")
            return
    print("User not found.")

def delete_user():
    try:
        id = int(input("Enter ID to delete: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return
    for user in users:
        if user["id"] == id:
            users.remove(user)
            print("User deleted.")
            return
    print("User not found.")

def menu():
    while True:
        print("\nChoose an operation:")
        print("1. Add user")
        print("2. Get user")
        print("3. Update user")
        print("4. Delete user")
        print("5. Show all users")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            create_user()
        elif choice == "2":
            read_user()
        elif choice == "3":
            update_user()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            print("All users:", users)
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

menu()
