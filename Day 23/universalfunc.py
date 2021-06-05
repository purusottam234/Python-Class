import numpy as np

numbers = np.array([1, 4, 9, 16, 25, 36])
print(np.sqrt(numbers))

numbers2 = np.arange(1, 7)*10
print(numbers2)

print(np.add(numbers, numbers2))
print(np.multiply(numbers2, 5))

numbers3 = numbers2.reshape(2, 3)
print(numbers3)
numbers4 = np.array([2, 4, 6])
print(np.multiply(numbers3, numbers4))
