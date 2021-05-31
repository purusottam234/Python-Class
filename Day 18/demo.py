grade_book = {
    'Ram': [98, 45, 66],
    'Hari': [83, 97, 98],
    'Lucky': [91, 89, 82],
    'Rahul': [97, 91, 92]
}

all_grades_count = 0
all_grades_total = 0

for name, grades in grade_book.items():
    total = sum(grades)
    print(f'Average for {name} is {total/len(grades): .2f}')
    all_grades_total += total
    all_grades_count += len(grades)
print(f" Class's average is : {all_grades_total/all_grades_count: .2f}")
