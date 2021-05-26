# Passing lists to function
def modify_elements(items):
    for i in range(len(items)):
        items[i] *= 2


numbers = [12, 23, 34, 55, 66]
modify_elements(numbers)
print(numbers)

numbers_tuple = (10, 20, 30)
print(numbers_tuple)
print(modify_elements(numbers_tuple))
