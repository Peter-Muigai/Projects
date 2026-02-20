file_name = 'pi_million_digit.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}")
print(len(pi_string))

birthday = input("Enter your birthday in the format dd/mm/yy: ")
if birthday in pi_string:
    print("Your birthday is in the first million digits of pi.")
else:
    print("Your birthday is not in the first million digits of pi.")