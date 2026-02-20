numbers = [10, 25, 67, 89, 32, 5, 48, 90]
less = list(filter(lambda x: x < 50, numbers))
print(less)

from functools import reduce
total = reduce(lambda x, y: x + y, less)
print(total)
