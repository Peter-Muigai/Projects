from typing import TextIO

students = []
for i in range(5):
    name = input(f"Enter name of student{i+1}:")
    score = float(input(f"Enter {name}'s score: "))
    students.append((name, score))

total = 0
for student in students:
    total += student[1]
average = total/len(students)
print(f"\nClass Average: {average:.2f}")

passed = []
failed = []
for name, score in students:
    if score >= 50:
        passed.append((name, score))
    else:
        failed.append((name, score))


print("\n✅ Passed Students:")
for name, score in students:
    if score >= 50:
        print(f"{name} - {score}")

print("\n❌ Failed Students:")
for name, score in students:
    if score < 50:
        print(f"{name} - {score}")

with open("student_results.txt", "w", encoding="utf-8") as file:
    file.write(f"Class Average: {average:.2f}\n\n")

    file.write("✅ Passed Students:\n")
    for name, score in passed:
        file.write(f"{name} - {score}\n")

    file.write("\n❌ Failed Students:\n")
    for name, score in failed:
        file.write(f"{name} - {score}\n")

print("\n📁 Results saved to 'student_results.txt'")