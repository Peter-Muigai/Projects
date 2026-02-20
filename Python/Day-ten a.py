print("Tip Calculator")
mySpend = int(input("How much did you spend?"))
myTip = int(input("How much percentage do you want to tip?"))
myGang = int(input("How many are you?"))
tip = (mySpend / myTip) / myGang
tip = round(tip, 2)
print("Your tip is:", tip)
