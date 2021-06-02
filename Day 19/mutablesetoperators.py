numbers = {1, 3, 5}
numbers |= {2, 5, 6}
print(numbers)

# update method

numbers.update(range(10))
# add method
numbers.add(10)
# remove method
numbers.remove(0)

# pop
numbers.pop()

# clear
numbers.clear()

print(numbers)
