# homogeneous data
c = [-45, 6, 0, 76, 89]
print(c)
# heterogeneous data

d = ['hari', 'ram', 3, 5]
print(d)

print(c[0])
print(c[1])
print(c[2])
print(c[3])
print(len(c))

print(c[4])

# negative indices
# indices always integers
print(c[-1])
print(c[-5])

print(c)
c[4] = 100
print(c)
# string does not support the item assigment
# s = "Hello"
# print(s[0])
# s[4] = "H"
# print(s[4])

# print(c[5])

a = c[0]+c[1]+c[3]
print(a)

# Append to a list with +=

a_list = []
for number in range(1, 6):
    a_list += [number]

print(a_list)

letters = []
letters += "Python"
print(letters)
