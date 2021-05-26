x = 10

print(id(x))


def cube(number):
    print('number is x:', number is x)
    return number**3


print(cube(x))


def cube(number):
    print('id(number) before modifying number:', id(number))
    number **= 3
    print('id(number) after modifying number:', id(number))
    return number


print(cube(x))
