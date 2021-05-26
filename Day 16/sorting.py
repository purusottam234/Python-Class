# sort method is used to sort or arrange its elements acending order
numbers = [10, 3, 4, 2, 1, 5, 6, 9, 8, 0]
numbers.sort()
print(numbers)
# we use reverse = true for descending order

numbers.sort(reverse=True)
print(numbers)

# sorted method returns new list containing sorted elements in sequence

numbers = [10, 3, 4, 2, 1, 5, 6, 9, 8, 0]
ascending_numbers = sorted(numbers)
print(ascending_numbers)
print(numbers)
letters = "sndshkjhjha"
ascending_letters = sorted(letters)
print(ascending_letters)
print(letters)

colors = ('red', 'orange', 'blue', 'yellow')
ascending_colors = sorted(colors)
print(ascending_colors)
print(colors)
