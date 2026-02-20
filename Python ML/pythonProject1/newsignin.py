import hashlib

max_attempts = 3
attempts = 0
logged_in = False

while True:
    print("\n=== Welcome ===")
    print("1. Sign Up")
    print("2. Log In")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        username = input("Enter a username: ")
        password = input("Enter a password: ")

        # Hash the password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Save to file
        with open("users.txt", "a") as file:
            file.write(f"{username}:{hashed_password}\n")

        print("✅ Sign Up successful! You can now log in.")

        print("Sign Up selected\n")
    elif choice == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Hash the entered password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Read from file
        found = False

        try:
            with open("users.txt", "r") as file:
                for line in file:
                    stored_username, stored_hash = line.strip().split(":")
                    if username == stored_username and hashed_password == stored_hash:
                        found = True
                        break
        except FileNotFoundError:
            print("No users found. Please sign up first.")

        if found:
            print("✅ Login successful. Welcome back,", username + "!")
        else:
            print("❌ Incorrect username or password.")

        print("Log In selected\n")
    elif choice == "3":
        print("Exiting program... Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

while attempts < max_attempts and not logged_in:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    found = False
    try:
        with open("users.txt", "r") as file:
            for line in file:
                stored_username, stored_hash = line.strip().split(":")
                if username == stored_username and hashed_password == stored_hash:
                    found = True
                    logged_in = True
                    break
    except FileNotFoundError:
        print("No users found. Please sign up first.")
        break

    if found:
        print("✅ Login successful. Welcome back,", username + "!")
    else:
        attempts += 1
        print(f"❌ Incorrect username or password. Attempts left: {max_attempts - attempts}")

if not logged_in and attempts == max_attempts:
    print("🚫 Too many failed attempts. Returning to main menu.")
