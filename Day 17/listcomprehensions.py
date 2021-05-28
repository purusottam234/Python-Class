list1 = []
for item in range(1, 6):
    list1.append(item)


print(list1)
# single line list comprehensions
list2 = [item for item in range(1, 6)]
print(list2)
# mapping
list3 = [item ** 3 for item in range(1, 6)]
print(list3)
# filtering
list4 = [item for item in range(1, 10) if item % 2 == 0]
print(list4)


colors = ['red', 'yellow', 'orange', 'green', 'blue']
colors2 = [item.upper() for item in colors]
print(colors2)
