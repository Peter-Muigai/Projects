exam_record = {
    "Alice": {"Score": 82},
    "Bob": {"Score": 74},
    "Charlie": {"Score": 90},
    "Diana": {"Score": 67}
}

exam_record["Ethan"] = {"Score": 88}
exam_record["Diana"] = {"Score": 76}

del exam_record["Bob"]

for student, info in exam_record.items():
    score = info["Score"]
    print(f"{student} -> Score: {score}")
