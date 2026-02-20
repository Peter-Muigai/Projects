print("Multiples of ten test")
number = input("Enter a number and I will tell you if it is a multiple of ten: ")
number = int(number)
if number %10 == 0:
    print("The number is a multiple of ten.")
else:
    print("The number is not a multiple of ten.")