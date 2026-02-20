print("=== Exam Grade Calculator ===")
num_exams = int(input("How many exams do you want to enter? "))

# To store results
exam_results = []

for i in range(num_exams):
    print(f"\nExam {i + 1}")
    exam_name = input("Name of exam: ")
    max_score = int(input("Maximum possible score: "))
    my_score = int(input("Your score: "))

    percentage = round((my_score / max_score) * 100, 0)

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

    # Store result
    exam_results.append({
        "name": exam_name,
        "score": my_score,
        "max": max_score,
        "percentage": percentage,
        "grade": grade
    })

# Final report
print("\n=== Grade Report ===")
for exam in exam_results:
    print(f"{exam['name']}: {exam['score']}/{exam['max']} = {exam['percentage']}% --> Grade: {exam['grade']}")
