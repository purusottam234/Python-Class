numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[2:7])
print(numbers[0:8])
print(numbers[0:])
print(numbers[6:])
print(numbers[:6])
print(numbers[:])
print(numbers[::2])
print(numbers[::5])
print(numbers[::-1])

b = numbers[0:3] = ["one ", "two", "three"]
print(b)
print(numbers)
# numbers[0:3] = []
# print(numbers)
numbers[::2] = [100, 100, 100, 100, 100]
print(numbers)
print(id(numbers))
