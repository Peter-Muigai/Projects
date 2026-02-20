print("Exam Grade Calculator")
myExam = input("Name of exam:")
myMax = int(input("The maximum possible score:"))
myScore = int(input("Your score:"))
answer = ((myScore / myMax) * 100)
answer = round(answer, 0)
print("Your score is", answer)
if answer == 90 or answer >= 90:
    print("That's an A+")
elif answer == 89 or answer >= 80:
    print("That's an A ")
elif answer == 79 or answer >= 70:
    print("That's a B")
elif answer == 69 or answer >= 60:
    print("That,s a C")
elif answer == 59 or answer >= 50:
    print("That's a D")
elif answer == 49 or answer >= 41:
    print("That's an E")
elif answer <= 40:
    print("You got a SUPP")
else:
    print("That's Ungraded")
