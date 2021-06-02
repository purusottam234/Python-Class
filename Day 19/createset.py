# Creating a set
colors = {"red", 'blue', 'yellow', 'green', 'red'}
print(colors)


# for length len function is used

print(len(colors))
# checking whether a value is in a set
print('white' in colors)

for color in colors:
    print(color.upper(), end=' ')

# use of built in set

numbers = list(range(10)) + list(range(5))

print(numbers)
print(set(numbers))


# creating empty set

# set()
