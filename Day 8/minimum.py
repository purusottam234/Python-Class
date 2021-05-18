# number1 = int(input("enter the first integer:"))
# number2 = int(input("enter the second integer:"))
# number3 = int(input("enter the third integer:"))
# minimum = number1
# if number2 < minimum:
#     minimum = number2

# if number3 < minimum:
#     minimum = number3

# print("Mimimum value is ", minimum)

# print(min(36, 27, 12))
# a = max(36, 27, 12)
# print(a)


numbers = [1, 2, 3, 4, 5, 1, 4, 5]

# start parameter is not provided
Sum = sum(numbers)
print(Sum)

# start = 10
Sum = sum(numbers, 10)
print(Sum)
