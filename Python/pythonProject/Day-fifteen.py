Exit = " "
while Exit != 'Yes':
    answer = input("What animal do you want to hear?")
    if answer == "Cow":
        print("A Cow goes moooo")
    elif answer == "Dog":
        print("A dog goes gooogooo")
    elif answer == "Sheep":
        print("A sheep goes meeeee")
    else:
        print("A an animal goes hoof!")
    print()
    Exit = input("Do you want to exit?")
    print("Exit")
