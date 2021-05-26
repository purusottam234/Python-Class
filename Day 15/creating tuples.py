# student_tuple = 'Harry', 'green'
# print(student_tuple)
# print(len(student_tuple))
# singleton tuple

singleton_tuple = ('red', 3)
print(singleton_tuple)


time_tuple = (2, 3, 5, 6)
print(time_tuple[0] * 3600 + time_tuple[1] * 60 + time_tuple[2])

# += augmented assignment

t1 = (12, 23, 34)
t2 = t1
print(t2)

t1 += (45, 47)
print(t1)
print(t2)

# appending tuples to lists +=

numbers = [1, 2, 3, 4, 5]
numbers += (6, 7)
print(numbers)

# Tuples may contains mutable objects
student_tuple = ("yellow", "blue", [98, 88, 45])
a = student_tuple[2][1] = 90
# print(student_tuple)
print(a)
print(student_tuple)
