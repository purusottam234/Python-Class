# index takes as an argument a search key ,value locate in the list

numbers = [2, 5, 6, 3, 4, 5, 8, 9, 7]
numbers.index(5)
numbers *= 3
print(numbers)
print(numbers.index(5, 7))  # first value
print(numbers.index(5, 7, len(numbers)))
print(numbers.index(5, 0, 7))

a = 1000 not in numbers
print(a)

key = 1000
if key in numbers:
    print(f'found {key} at index {numbers.index(key)}')
else:
    print(f'{key} not found')
