def maximum(value1, value2, value3):
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value


print(maximum(12, 34, 45))
print(maximum(12, 34, -45))
print(maximum('yellow', 'red', 'blue'))
