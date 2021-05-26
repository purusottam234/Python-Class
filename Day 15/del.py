# del statement can be used to remove elements from a list
#  and to delete variables from interactive session

numbers = list(range(0, 10))
print(numbers)
del numbers[-1]
print(numbers)

del numbers[0:2]
print(numbers)

del numbers[:2]
print(numbers)
