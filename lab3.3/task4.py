users = {}

def register_user():
    """
    Function to register a new user by collecting username and password.
    Includes validation and duplicate username checking.
    """
    print("User Registration")
    print("=" * 20)
    
    while True:
        # Get username from user
        username = input("Enter username: ").strip()
        
        # Validate username
        if not username:
            print("Username cannot be empty. Please try again.")
            continue
        
        # Check if username already exists
        if username in users:
            print("Username already exists. Please choose a different one.")
            continue
        
        # Username is valid and unique
        break
    
    while True:
        # Get password from user
        password = input("Enter password: ").strip()
        
        # Validate password
        if not password:
            print("Password cannot be empty. Please try again.")
            continue
        
        # Check password length (basic security)
        if len(password) < 6:
            print("Password must be at least 6 characters long.")
            continue
        
        # Get password confirmation
        confirm_password = input("Confirm password: ").strip()
        
        # Check if passwords match
        if password != confirm_password:
            print("Passwords do not match. Please try again.")
            continue
        
        # Password is valid and confirmed
        break
    
    # Store user credentials in the dictionary
    # WARNING: In real applications, NEVER store passwords as plain text!
    # Use password hashing libraries like bcrypt or hashlib
    users[username] = password
    
    print(f"\nUser '{username}' registered successfully!")
    print(f"Total users registered: {len(users)}")

def login_user():
    """
    Function to authenticate a user by checking username and password.
    Returns True if login successful, False otherwise.
    """
    print("User Login")
    print("=" * 15)
    
    # Get username from user
    username = input("Enter username: ").strip()
    
    # Check if username exists
    if username not in users:
        print("Username not found. Please register first.")
        return False
    
    # Get password from user
    password = input("Enter password: ").strip()
    
    # Check if password matches the stored password
    # WARNING: This is plain text comparison - NOT secure for production!
    if users[username] == password:
        print(f"\nWelcome back, {username}! Login successful.")
        return True
    else:
        print("Incorrect password. Please try again.")
        return False

def main():
    """
    Main function to demonstrate the user authentication system.
    Provides a menu to register, login, or exit.
    """
    print("User Authentication System")
    print("=" * 30)
    
    while True:
        print("\n1. Register User")
        print("2. Login User")
        print("3. View Registered Users")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            register_user()
            
        elif choice == '2':
            login_user()
            
        elif choice == '3':
            if users:
                print(f"\nRegistered Users ({len(users)}):")
                for username in users.keys():
                    print(f"- {username}")
            else:
                print("\nNo users registered yet.")
                
        elif choice == '4':
            print("\nThank you for using the User Authentication System!")
            break
            
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
1