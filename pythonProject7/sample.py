file = open("diary.txt", "w")
entry = input("Enter your diary entry:")
file.write(entry + "\n")
file.close()

file = open("diary.txt", "r")
content = file.read()
print("Your diary now contains:\n" + content)
file.close()