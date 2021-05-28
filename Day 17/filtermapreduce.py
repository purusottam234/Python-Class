

# built in filter and map for filtering and Mapping

# reductions use in a Collection of elements into a single value such as

# count ,total,product ,average etc

# filter method

numbers = [10, 2, 3, 4, 5, 6, 7, 9]


def is_odd(x):
    return x % 2 != 0


print(list(filter(is_odd, numbers)))
# if clause

print([item for item in numbers if is_odd(item)])

# lambda is an anonymous function that is a function without a name
# we use lambda expression  to define function inline where
# it's needed typically
# as it's passed to another function

print(list(filter(lambda x: x % 2 != 0, numbers)))

# function :

# def function_name(parameter_list):
#     return expression

# lambda :
# lambda parameter_list: expression
print(numbers)
print(list(map(lambda x: x**2, numbers)))

print([item ** 2 for item in numbers])


# combining filter and map function with lambda

print(list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, numbers))))
print([x**2 for x in numbers if x % 2 != 0])
