# Open file for writing
file = open("example.txt", "w")
file.write("Hello Peter!\nWelcome to File Handling in Python.")
file.close()

# Open file for reading
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
