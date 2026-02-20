import datetime

def add_task():
    task = input("Enter your task: ")
    now = datetime.datetime.now()
    with open("log.txt", "a") as file:
        file.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')} - {task}\n")
    print("✅ Task added!\n")

def view_tasks():
    print("\n📄 Your Tasks:\n")
    try:
        with open("log.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("⚠️ No task log found.\n")

def menu():
    while True:
        print("\nWelcome to Daily Task Logger!")
        print("1. Add new task")
        print("2. View tasks")
        print("3. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid input, try again.\n")

menu()
