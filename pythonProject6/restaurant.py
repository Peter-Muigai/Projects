prompt = "Hello and welcome to PEMU INN:"
prompt += "How many people are in the dinner group? "
number = input(prompt)
number = int(number)
if number > 8:
    print("You will have to wait for a table")
else:
    print('There is a table for you.')