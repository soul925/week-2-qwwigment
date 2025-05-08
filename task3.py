import hashlib
import getpass

user_db = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    if username in user_db:
        print("User already exists!")
    else:
        user_db[username] = hash_password(password)
        print("New user created")

def login(username, password):
    hashed = hash_password(password)
    if username in user_db and user_db[username] == hashed:
        print("Login Successful")
    else:
        print("Invalid credentials")

while True:
    action = input("Do you want to register or login? (type 'register', 'login' or 'exit'): ").strip().lower()
    
    if action == 'exit':
        break
    elif action in ['register', 'login']:
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        
        if action == 'register':
            register(username, password)
        elif action == 'login':
            login(username, password)
    else:
        print("Invalid option, please type 'register', 'login' or 'exit'.")
