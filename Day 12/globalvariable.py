x = 10
# use keyword global inside a function to modify global variable
#  or to make global variable from function


def access_global():
    global x
    x = 5  # local variable
    print("x  printed from local:", x)


print(access_global())
print(x)
