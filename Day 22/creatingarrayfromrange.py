# arange

import numpy as np
print(np.arange(5, 10))
print(np.arange(10, 1, -2))

# creating floating point ranges with linspace

print(np.linspace(0.0, 1.0, num=5))

# reshaping an array

print(np.arange(1, 21).reshape(4, 5))

# display large array

print(np.arange(1, 100001).reshape(4, 25000))
print(np.arange(1, 100001).reshape(100, 1000))
