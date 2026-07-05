numbers = [10, 15, 30, 45, 50, 60, 75]

result = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers))

print("Original list :", numbers)

print("Divisible by 3 and 5:",result)