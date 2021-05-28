from typing import Iterable


# Generator Expression is similar to list comprehension but creates an Iterable
# generator object that produce on demand,also known as lazy  evaluation


# importance : reduce memory consumption and improve performance
# use parenthesis inplace of square bracket
# This method doesnot create a list
numbers = [10, 2, 3, 4, 5, 6, 7, 9, 10]
for value in (x**2 for x in numbers if x % 2 != 0):
    print(value, end=' ')

squares_of_odds = (x ** 2 for x in numbers if x % 2 != 0)
print(squares_of_odds)
