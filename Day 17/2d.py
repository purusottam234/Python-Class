# multidimensional list is a list which is represented in table ,arrange in
# row and colums
# lists requires two indices to identify an elements

a = [[77, 88, 90, 23], [96, 68, 45, 34], [80, 70, 56, 45]]

# a = [[77, 88, 90, 23],
#      [96, 68, 45, 34],
#      [80, 70, 56, 45]]

for row in a:
    for item in row:
        print(item, end=" ")
        print()

for i, row in enumerate(a):
    for j, item in enumerate(row):
        print(f'a[{i}][{j}] = {item}', end=' ')
    print()
