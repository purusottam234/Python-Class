# pseudo code
# if student'grade is greater than or equal to 90
# display "A"
# else if student'grade is greater than or equal to 80
# display "B"
# else if student'grade is greater than or equal to 70
# display "C"
# else if student'grade is greater than or equal to 60
# display "D"
# else
# display "E"

# Python implementation


grade = int(input("Enter your marks:"))
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("E")
