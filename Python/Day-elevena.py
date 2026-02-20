year = int(input("Which year do you want to calculate? "))
hour = 60 * 60
day = 24 * hour
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
  days = 366
  seconds = days * day
  print("Leap Year:", seconds, "seconds")
else:
  days = 365
  seconds = days * day
  print(seconds, "seconds")