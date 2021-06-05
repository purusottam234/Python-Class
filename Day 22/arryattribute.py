import numpy as np

integers = np.array([[1, 3, 5, 4], [5, 6, 10, 8]])
print(integers)

floats = np.array([0.0, 1.0, 0.4, 0.5])
print(floats)

# determining an array's element type

print(integers.dtype)
print(floats.dtype)

# dimension ndim method
print(integers.ndim)
print(floats.ndim)

# shape
print(integers.shape)
print(floats.shape)
# number of elements

print(integers.size)
print(floats.size)

# iterating multidimensional array's elements

for row in integers:
    for column in row:
        print(column, end=" ")
    print()

for i in integers.flat:
    print(i, end=" ")
