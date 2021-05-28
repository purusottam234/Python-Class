# Create a list called numbers containing 1 through 15, then perform
# the following tasks:
# a. Use the built in function filter with lambda to select only numbers even elements function.
#   Create a new list containing the result

# b.Use the built in function map with a lambda to square the values of numbers' elements. Create
#  a new list containing the result function

# c. Filter numbers even elements , then map them to their squares .Create
#   a new list containing  the  result

numbers = list(range(1, 16))
print(numbers)
a = list(filter(lambda x: x % 2 == 0, numbers))
print(a)
b = list(map(lambda x: x ** 2, numbers))
print(b)
c = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(c)
