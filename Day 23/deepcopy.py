import numpy as np

numbers = np.arange(1, 6)
print(numbers)
numbers2 = numbers.copy()
print(numbers2)

numbers[1] *= 10
print(numbers)
