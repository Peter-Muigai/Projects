prompt = "\nEnter the toppings you want to add on your pizza"
prompt += "\n(Enter quit to stop:) "
while True:
    toppings = input(prompt)
    if toppings == 'quit':
        break
    else:
        print(f"You have added {toppings} on your pizza.")