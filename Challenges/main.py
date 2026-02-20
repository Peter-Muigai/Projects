start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

word3 = input("Word for multiples of 3: ")
word5 = input("Word for multiples of 5: ")

for i in range(start, end + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(word3 + word5)
    elif i % 3 == 0:
        print(word3)
    elif i % 5 == 0:
        print(word5)
    else:
        print(i)
