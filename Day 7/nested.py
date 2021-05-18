passes = 0
failures = 0

for student in range(10):
    result = int(input("enter the result (1 = pass,2= false):"))
    if result == 1:
        passes = passes+1
    else:
        failures = failures+1


print("passes:", passes)
print("failures:", failures)
if passes > 8:
    print("bonus to teacher")
