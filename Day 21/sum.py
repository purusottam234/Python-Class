def sum(*numbers):
    output = 0
    for number in numbers:
        output += number
    return output


print(sum(10, 20, 30, 10, 20, 30))
