names = ['John', 'Mark', 'Robert', 'Jenna']
print(names)
message = f"I am pleased to invite you {names[0]} to dinner this Monday."
print(message)
message = f"I am pleased to invite you {names[1]} to dinner this Monday."
print(message)
message = f"I am pleased to invite you {names[2]} to dinner this Monday."
print(message)
message = f"I am pleased to invite you {names[3]} to dinner this Monday."
print(message)
print(f"I have been notified that {names[1]} will not be able to attend dinner. ")
names[1] = 'Steph'
print(names)
message = f"I am pleased to invite you {names[0]} to dinner this Monday."
print(message)
message = f"I am pleased to invite you {names[1]} to dinner this Monday."
print(message)
message = f"I am pleased to invite you {names[2]} to dinner this Monday."
print(message)
message = f"I am pleased to invite you {names[3]} to dinner this Monday."
print(message)
print("A larger dinner table is now available which means our dinner can have more people.")
names.insert(0, 'Kevin')
print(names)
names.insert(2, 'Mike')
print(names)
names.append('Elton')
print(names)
message = f"I am pleased to invite you {names[0]} to dinner this Monday."
print(message)
message = f"I am pleased to invite you {names[1]} to dinner this Monday."
print(message)
message = f"I am pleased to invite you {names[2]} to dinner this Monday."
print(message)
message = f"I am pleased to invite you {names[3]} to dinner this Monday."
print(message)
message = f"I am pleased to invite you {names[4]} to dinner this Monday."
print(message)
message = f"I am pleased to invite you {names[5]} to dinner this Monday."
print(message)
message = f"I am pleased to invite you {names[6]} to dinner this Monday."
print(message)
print("I am very sorry the larger dinner table will not be available, "
      "hence I can only invite two guests to my dinner")
popped_names = names.pop()
print(names)
popped_names = names.pop()
print(names)
popped_names = names.pop()
print(names)
popped_names = names.pop()
print(names)
popped_names = names.pop()
print(names)
message = f"{names[0]}, are still invited to my dinner."
print(message)
message = f"{names[1]}, are still invited to my dinner."
print(message)
del names[0]
print(names)
del names[0]
print(names)