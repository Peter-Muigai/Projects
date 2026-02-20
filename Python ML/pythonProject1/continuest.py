while True:
    print("You are in a corridor, do you go Right or Left?")
    direction = input("> ")
    if direction == "Left":
        print("You have fallen tou your death!!")
        break
    elif direction == "Right":
        continue
    else:
        print("Ahh!You are a genius, you have won!")
        exit()
print("The game is over!, you have failed!!!")
