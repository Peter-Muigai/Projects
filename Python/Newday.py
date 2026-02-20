print("Exam Grade Calculator")
myExam = input("Name of exam: ")
myMax = int(input("The maximum possible score: "))
myScore = int(input("Your score: "))

answer = (myScore / myMax) * 100
answer = round(answer, 0)

print("Your score is", answer, "%")

if answer >= 90:
    print("That's an A+")
elif answer >= 80:
    print("That's an A")
elif answer >= 70:
    print("That's a B")
elif answer >= 60:
    print("That's a C")
elif answer >= 50:
    print("That's a D")
elif answer >= 41:
    print("That's an E")
elif answer <= 40:
    print("You got a SUPP")