numbers = [1, 2, 3, 4]

numbers.clear()

print(numbers)

numbers = [1, 2, 3, 4]

del numbers[0:4]

print(numbers)


numbers = [1, 2, 3, 4]

while numbers:
    numbers.pop()

print(numbers)