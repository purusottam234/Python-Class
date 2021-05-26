# we create a bar chart where bar's  length is made of asterisks(*)

numbers = [23, 45, 56, 12, 26]
print("\nCreating a bar chart from numbers: ")
print(f'Index{"value":>8} Bar')

for index, value in enumerate(numbers):
    print(f'{index:>5}{value:>8} {"*" *value}')
