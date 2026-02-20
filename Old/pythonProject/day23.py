def rollDice():
    import random
    dice = random.randint(1, 6)
    print("You rolled", dice)

for i in range(10):
    rollDice()
