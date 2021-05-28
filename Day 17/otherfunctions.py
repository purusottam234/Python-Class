# max and min function
#  print("red" < 'orange')
# print(ord('r'))
# print(ord('o'))
colors = ['red', 'yellow', 'orange', 'green', 'blue']
print(min(colors, key=lambda s: s.lower()))
print(max(colors, key=lambda s: s.lower()))

# reversed iterates from backward

numbers = [10, 2, 3, 4, 5, 6, 7, 9]
reversed_numbers = [item for item in reversed(numbers)]
print(reversed_numbers)

# zip function iterate over multiple iterables of data at the same time
names = ['bob', 'ram', 'hari', 'sita']
grade_point_averages = [3.5, 4.0, 3.74, 2.98]
for name, gpa in zip(names, grade_point_averages):
    print(f'Name = {name}: GPA = {gpa}')
