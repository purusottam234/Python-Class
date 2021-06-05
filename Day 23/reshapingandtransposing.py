import numpy as np

grades = np.array([[87, 96, 70], [100, 87, 90]])
print(grades)
# print(grades.reshape(1, 6))
# print(grades)

# print(grades.resize(1, 6))
# print(grades)

# flatten vs ravel

# flattened = grades.flatten()
# print(flattened)
# print(grades)


# raveled = grades.ravel()
# print(raveled)
# print(grades)

# print(grades.T)
# print(grades)
# horizontal and vertical stacking

grades2 = np.array([[11, 20, 30], [44, 54, 64]])
print(np.hstack((grades, grades2)))
print(np.vstack((grades, grades2)))
