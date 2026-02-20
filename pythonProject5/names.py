names = ['peter', 'kevin', 'john', 'mark', 'will']
message = f"I wish {names[-1].title()} was my girl."
print(names[-3])
print(message)
names[0] = 'martin'
print(names)
names.append('chris')
print(names)
names.insert(2, 'jane')
print(names)
del names[1]
print(names)
popped_names = names.pop()
print(names)
print(popped_names)
names.remove('mark')
print(names)