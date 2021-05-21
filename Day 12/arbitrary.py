def average(*args):
    return sum(args)/len(args)


# print(average(5, 10))
# print(average(5, 10, 23, 45, 67, 89, 10))

# Note *args = rightmost parameter
grades = [89, 34, 56, 78, 23, 46, 90]

print(average(*grades))
