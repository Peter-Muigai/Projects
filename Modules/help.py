class Tracker:
    def __init__(self):
        # Core persistent data
        self.students = []    # Each student will be a dictionary with 'name', 'reg', and 'results'
        self.subjects = []    # List of subject names

    # Add new students
    def add_student(self):
        num = int(input("How many students do you want to add? "))
        for _ in range(num):
            name = input("Enter student name: ")
            reg = input("Enter student registration number: ")
            # Initialize results dictionary for this student
            self.students.append({
                "name": name,
                "reg": reg,
                "results": {}   # Stores subject results later
            })
            print(f"{name} ({reg}) added successfully.")

    # Add subjects to the class
    def add_subject(self):
        num = int(input("How many subjects do you want to enter? "))
        for _ in range(num):
            subject = input("Enter subject name: ")
            self.subjects.append(subject)
            print(f"{subject} added successfully.")

    # Calculate student performance
    def calculate(self):
        for student in self.students:
            print(f"\nEntering results for {student['name']} ({student['reg']})")
            for subject in self.subjects:
                max_score = int(input(f"Maximum score for {subject}: "))
                score = int(input(f"{student['name']}'s score in {subject}: "))
                percentage = round((score / max_score) * 100, 2)

                # Determine grade
                if percentage >= 90:
                    grade = "A+"
                elif percentage >= 80:
                    grade = "A"
                elif percentage >= 70:
                    grade = "B"
                elif percentage >= 60:
                    grade = "C"
                elif percentage >= 50:
                    grade = "D"
                elif percentage >= 41:
                    grade = "E"
                else:
                    grade = "SUPP"

                # Store result under this student
                student["results"][subject] = {
                    "score": score,
                    "max": max_score,
                    "percentage": percentage,
                    "grade": grade
                }

    # Display all student performance
    def show_all(self):
        print("\n=== STUDENT PERFORMANCE REPORT ===")
        for student in self.students:
            print(f"\nStudent: {student['name']} ({student['reg']})")
            print("-" * 40)
            for subject, data in student["results"].items():
                print(f"{subject}: {data['score']}/{data['max']} "
                      f"({data['percentage']}%) --> Grade: {data['grade']}")

    # Display student names
    def display_students(self):
        print("\n=== STUDENTS LIST ===")
        for idx, student in enumerate(self.students, 1):
            print(f"{idx}. {student['name']} ({student['reg']})")

def add_student(self):
    num = int(input("How many students do you want to enter? "))
    for _ in range(num):
        name = input("Enter student name: ")
        reg = input("Enter student registration number: ")

        self.students.append({
            "name": name,
            "reg": reg,
            "results": {}
        })
        print(f"{name} ({reg}) added successfully.")
def add_subject(self):
    num = int(input("How many subjects do you want to enter? "))
    for _ in range(num):
        subject = input("Enter subject name: ")
        self.subjects.append(subject)
def calculate(self):
    """Calculate results for each student and each subject."""
    for student in self.students:
        print(f"\nEntering results for {student['name']} ({student['reg']})")

        for subject in self.subjects:
            max_score = int(input(f"Maximum score for {subject}: "))
            score = int(input(f"{student['name']}'s score in {subject}: "))

            percentage = round((score / max_score) * 100, 2)

            if percentage >= 90:
                grade = "A+"
            elif percentage >= 80:
                grade = "A"
            elif percentage >= 70:
                grade = "B"
            elif percentage >= 60:
                grade = "C"
            elif percentage >= 50:
                grade = "D"
            elif percentage >= 41:
                grade = "E"
            else:
                grade = "SUPP"

            # ✅ Store per student
            student["results"][subject] = {
                "score": score,
                "max": max_score,
                "percentage": percentage,
                "grade": grade
            }
def show_all(self):
    print("\n===== STUDENT PERFORMANCE REPORT =====")
    for student in self.students:
        print(f"\nStudent: {student['name']} ({student['reg']})")
        print("-" * 40)

        for subject, data in student["results"].items():
            print(f"{subject}: {data['score']}/{data['max']} "
                  f"({data['percentage']}%) --> Grade: {data['grade']}")

def main():
    tracker = Tracker()

    while True:
        print("\nWelcome to Student Performance Tracker.")
        print("1. Add Student(s)")
        print("2. Add Subject(s)")
        print("3. Calculate Student(s) Performance")
        print("4. View Students Performance.")
        print("5. View Class Summary.")
        print("6. Quit.")

        choice = input("Choose from the options(1-6): ")
        if choice == '1':
            tracker.add_student()
        elif choice == '2':
            tracker.add_subject()
        elif choice == '3':
            tracker.calculate()
        elif choice == '4':
            tracker.display_students()
        elif choice == '5':
            tracker.show_all()
        elif choice == '6':
            print("Leaving so soon?")
            break
        else:
            break


if __name__ == "__main__":
    main()
