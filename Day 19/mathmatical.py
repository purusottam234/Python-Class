# union of two sets is a consisting of all the unique elements of both sets

# a = {1, 2, 3} | {2, 3, 4}
# print(a)

# b = {1, 2, 3}.union([20, 3, 2, 5])
# print(b)

# intersection of two sets is a consisting of all the unique elements of both sets have in common

# c = {1, 2, 3} & {2, 3, 4}
# print(c)

# d = {1, 2, 3}.intersection([20, 3, 2, 5])
# print(d)
# Difference of two sets is a consisting of  elements in
# the left operand that are not in right operand

# a = {1, 2, 3} - {2, 3, 4}
# print(a)

# b = {1, 2, 3}.difference([20, 3, 2, 5])
# print(b)
# Symmetric difference between two sets is a set consiting the elements of both sets that are
# not in common with one another
# a = {1, 2, 3} ^ {2, 3, 4}
# print(a)

# b = {1, 2, 3}.symmetric_difference([20, 3, 2, 5])
# print(b)
# Two sets are disjoint if they do not have any common elements
a = {1, 6, 5} .isdisjoint({2, 3, 4})
print(a)

b = {1, 2, 3}.isdisjoint({20, 3, 2, 5})
print(b)
