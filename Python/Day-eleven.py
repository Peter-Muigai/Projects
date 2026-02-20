print('Below is a calculator that will enable us calculate number of seconds in an year')
myYear = input("Which year do you want to calculate?")
hour = 60 * 60
day = 24
year = 365
seconds = day * hour * year
if myYear == "Normal year":
    seconds = day * hour * year
    print("There are", seconds)
elif myYear == "Leap year":
    seconds = day * hour * (year + 1)
    print("There are", seconds)
else :
    print("Try asking your question right")
