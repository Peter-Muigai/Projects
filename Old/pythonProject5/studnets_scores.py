students = []
def load_students_from_file():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                name, score = line.strip().split(",")
                students.append((name, int(score)))
        print("Students loaded from 'students.txt'.")
    except FileNotFoundError:
        print("No saved data found. Starting fresh.")
load_students_from_file()


def add_student():
    name = input("Enter student name: ")
    try:
        score = int(input("Enter student score: "))
        students.append((name, score))
        print(f"{name} added successfully!\n")
    except ValueError:
        print("Invalid score! Please enter a number.\n")
    input("Press Enter to return to menu...")

def view_all_students():
    if not students:
        print("No students added yet.")
    else:
        print("\nAll Students:")
        for name, score in students:
            print(f"{name} - {score}")
    input("Press Enter to return to menu...")

def view_passed_students():
    passed = [s for s in students if s[1] >= 50]
    if not passed:
        print("No students have passed yet.")
    else:
        print("\nPassed Students:")
        for name, score in passed:
            print(f"{name} - {score}")
    input("Press Enter to return to menu...")

from functools import reduce

def get_summary_data():
    if not students:
        return 0, 0, ("None", 0), ("None", 0)

    total = reduce(lambda acc, s: acc + s[1], students, 0)
    average = total / len(students)
    top = max(students, key=lambda s: s[1])
    bottom = min(students, key=lambda s: s[1])

    return total, average, top, bottom

def view_summary():
    total, average, top, bottom = get_summary_data()

    if total == 0:
        print("No data to summarize.")
    else:
        print("\n--- Score Summary ---")
        print(f"Total Score: {total}")
        print(f"Average Score: {average:.2f}")
        print(f"Top Scorer: {top[0]} - {top[1]}")
        print(f"Lowest Scorer: {bottom[0]} - {bottom[1]}")
    input("Press Enter to return to menu...")

def save_students_to_file():
    with open("students.txt", "w") as file:
        for name, score in students:
            file.write(f"{name},{score}\n")
    print("Students saved to 'students.txt'.")
    input("Press Enter to return to menu...")
while True:
    print("\n--- Student Analyzer Menu ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. View Passed Students")
    print("4. View Summary")
    print("5. Save to File")
    print("6. Exit")


    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_all_students()
    elif choice == "3":
        view_passed_students()
    elif choice == "4":
        view_summary()
    elif choice == "5":
        save_students_to_file()
    elif choice == "6":
        print("Goodbye, Peter!")
        break

