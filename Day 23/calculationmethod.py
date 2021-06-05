import numpy as np

grades = np.array([[23, 45, 67], [100, 87, 34], [56, 66, 23], [100, 81, 82]])
print(grades)

print(grades.sum())
print(grades.min())
print(grades.max())
print(grades.mean())
print(grades.std())
print(grades.var())
print(grades.mean(axis=0))
print(grades.mean(axis=1))
