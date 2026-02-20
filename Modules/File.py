class Tracker:
    def __init__(self):
        self.students = []    # Each student: {name, reg, results}
        self.subjects = []    # List of subject names

    # ---------------- STUDENT & SUBJECT MANAGEMENT ----------------
    def add_student(self):
        num = int(input("How many students do you want to add? "))
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
            print(f"{subject} added successfully.")

    # ---------------- PERFORMANCE CALCULATION ----------------
    def calculate(self):
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

                student["results"][subject] = {
                    "score": score,
                    "max": max_score,
                    "percentage": percentage,
                    "grade": grade
                }

    # ---------------- INDIVIDUAL REPORT ----------------
    def show_all(self):
        print("\n=== STUDENT PERFORMANCE REPORT ===")
        for student in self.students:
            print(f"\nStudent: {student['name']} ({student['reg']})")
            print("-" * 40)
            for subject, data in student["results"].items():
                print(f"{subject}: {data['score']}/{data['max']} "
                      f"({data['percentage']}%) --> Grade: {data['grade']}")

    # ---------------- CLASS SUMMARY ----------------
    def class_summary(self):
        print("\n=== CLASS SUMMARY ===")

        # Average per subject
        for subject in self.subjects:
            total = 0
            count = 0
            highest = None
            lowest = None
            top_student = None

            for student in self.students:
                if subject in student['results']:
                    score = student['results'][subject]['percentage']
                    total += score
                    count += 1

                    if highest is None or score > highest:
                        highest = score
                        top_student = student['name']
                    if lowest is None or score < lowest:
                        lowest = score

            if count > 0:
                average = round(total / count, 2)
                print(f"\nSubject: {subject}")
                print(f"Average Score: {average}%")
                print(f"Top Student: {top_student} ({highest}%)")
                print(f"Lowest Score: {lowest}%")

    # ---------------- SAVE DATA ----------------
    def save_to_file(self, filename="results.txt"):
        with open(filename, "w") as file:
            for student in self.students:
                file.write(f"{student['name']}|{student['reg']}\n")
                for subject, data in student['results'].items():
                    file.write(f"{subject},{data['score']},{data['max']},{data['percentage']},{data['grade']}\n")
                file.write("---\n")
        print("Data saved successfully.")

    # ---------------- LOAD DATA ----------------
    def load_from_file(self, filename="results.txt"):
        self.students = []
        current_student = None

        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line == "---":
                    current_student = None
                elif "|" in line:
                    name, reg = line.split("|")
                    current_student = {"name": name, "reg": reg, "results": {}}
                    self.students.append(current_student)
                else:
                    subject, score, max_score, percentage, grade = line.split(",")
                    current_student['results'][subject] = {
                        "score": int(score),
                        "max": int(max_score),
                        "percentage": float(percentage),
                        "grade": grade
                    }

        print("Data loaded successfully.")


# ---------------- MAIN MENU ----------------

def main():
    tracker = Tracker()

    while True:
        print("\n===== STUDENT PERFORMANCE TRACKER =====")
        print("1. Add Students")
        print("2. Add Subjects")
        print("3. Enter Results & Calculate")
        print("4. View Individual Reports")
        print("5. View Class Summary")
        print("6. Save Data")
        print("7. Load Data")
        print("8. Exit")

        choice = input("Choose option (1-8): ")

        if choice == "1":
            tracker.add_student()
        elif choice == "2":
            tracker.add_subject()
        elif choice == "3":
            tracker.calculate()
        elif choice == "4":
            tracker.show_all()
        elif choice == "5":
            tracker.class_summary()
        elif choice == "6":
            tracker.save_to_file()
        elif choice == "7":
            tracker.load_from_file()
        elif choice == "8":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
