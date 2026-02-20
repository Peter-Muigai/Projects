with open("tasks.txt", "w")as file:
    file.write("1. Complete my assignments.\n")
    file.write("2. Complete my python assignment.\n")
    file.write("3. Submit my work on time.")

with open("tasks.txt", "a") as file:
    file.write("\n4. Review file handling concepts.")
with open("tasks.txt", "a") as file:
    file.write("\n5. Write new test for my projects")
with open("tasks.txt", "a") as file:
    file.write("\n6. Review my coming week exams.")

with open("tasks.txt", "r") as file:
    content = file.read()
    print(content)
