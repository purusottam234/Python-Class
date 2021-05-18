# 1.Use for statement to input two integers. Use nested if ..else statement to
# display whether each value is even or odd. Enter 10 and 7 to test your code.

for count in range(2):
    value = int(input("enter an integer: "))
    if value % 2 == 0:
        print(f'{value} is even')
    else:
        print(f'{value} is odd')


# 2. Use for and range function to sum the even integers from 2 through 100 display their sum.

total = 0
for number in range(2, 101, 2):
    total += number
print(total)
