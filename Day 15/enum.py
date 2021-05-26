# enumerate provides indexing and value

colors = ['red', 'orange', 'blue']
print(list(enumerate(colors)))

# built in function tuple is used to create a tuple

print(tuple(enumerate(colors)))

for index, value in enumerate(colors):
    print(f'{index}:{value}')
