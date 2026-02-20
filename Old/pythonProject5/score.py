from functools import reduce

students = [
    ("Alice", 78),
    ("Bob", 45),
    ("Charlie", 66),
    ("Diana", 32),
    ("Ethan", 90)
]
passed_students = list(filter(lambda x: x[1] >= 50, students))
print("Passed students:", passed_students)
total_score = reduce(lambda x, y: x + y[1], students, 0)
print("Total score:", total_score)
average_score = total_score / len(students)
print("Average Score:", average_score)

top_scorer = max(students, key=lambda x: x[1])
print(f"Top Scorer: {top_scorer[0]} - {top_scorer[1]}")

bottom_scorer = min(students, key=lambda x: x[1])
print(f"Lowest Scorer: {bottom_scorer[0]} - {bottom_scorer[1]}")
