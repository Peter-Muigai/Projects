while True:
    print("You are in a corridor where do you go?Left or Right")
    direction = input(">")
    if direction == "Left":
        print("You have fallen to your death!")
        break
    elif direction == "Right":
        continue
    else:
        print("Aww!You are a genius you've won!")
        exit()
print("You've failed the game is over!!!")