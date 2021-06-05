import numpy as np

numbers = np.arange(1, 6)
print(numbers)

numbers2 = numbers.view()
print(numbers2)
print(id(numbers))
numbers2 = numbers[0:3]
print(numbers2)
print(id(numbers2))
print(numbers[3])
