report_card = {
    "Alice": {"Math": 82, "Physics": 78, "English": 85},
    "Bob": {"Math": 74, "Physics": 80, "English": 72},
    "Charlie": {"Math": 90, "Physics": 88, "English": 95},
    "Diana": {"Math": 67, "Physics": 60, "English": 70}
}

report_card["Ethan"] = {"Math": 88, "Physics": 85, "English": 90}

report_card["Diana"]["English"] = 76

del report_card["Bob"]

for student, subjects in report_card.items():
    average = sum(subjects.values()) / len(subjects)
    print(f"{student} -> Average Score: {average:.2f}")

top_student = ""
top_avg = 0

for student, subjects in report_card.items():
    avg = sum(subjects.values()) / len(subjects)
    if avg > top_avg:
        top_avg = avg
        top_student = student

print(f"\n🏆 Top Student: {top_student} with an average score of {top_avg:.2f}")
