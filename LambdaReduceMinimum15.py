from functools import reduce

numbers = [10, 50, 30, 40, 35, 25]

result = reduce(lambda x, y: x if x < y else y, numbers)

print("Original List :",numbers)

print("Minimum Element :", result)