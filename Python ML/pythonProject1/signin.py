import hashlib

max_attempts = 3
attempts = 0
logged_in = False

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
