numbers = [10, 23, 45, 65, 82, 27]

even_count = list(filter(lambda x: x % 2 == 0, numbers))

print("Original list :", numbers)

print("Count of Even numbers :",even_count)