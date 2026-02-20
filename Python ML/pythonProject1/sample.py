print("Lyrics generator")
print("Fill in the blanks")
counter = 0
while True:
    trial = input("Could you let me____slowly")
    if trial != "down":
        print("Nope,try again")
        max_attempts = 3
        attempts = 0

        while attempts > max_attempts:
            print("Try again")
        if trial == "yes":
            break
    elif trial == "down":
        print("There there")
print("Come  back soon")