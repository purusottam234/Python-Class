# 1. program to determine the first power of 7 greater than 1000
product = 7
while product <= 1000:
    product = product * 7
print(product)

# 2.Use the range function and a for statement to calculate the total of the integer from 0 to 1000000
total = 0
for number in range(1000001):
    total += number
print(total)
# 3.Display f-string in which you insert the value of the variables number1(7) and number2(5) and their product. display string should be:
#     7 times 5 is 35

number1 = 7
number2 = 5
mul = number1*number2
print(f'{number1} times {number2} is {mul}')
