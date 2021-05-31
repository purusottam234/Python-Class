# Converting dictionary to lists
months = {'january': 31, 'february': 30, 'march': 31}

print(list(months.keys()))
print(list(months.values()))

print(list(months.items()))

# processing keys in sorted order
for month_name in sorted(months.keys()):
    print(month_name, end=" ")

for month_name in sorted(months.values()):
    print(month_name, end=" ")
