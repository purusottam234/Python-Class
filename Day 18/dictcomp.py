months = {"jan": 1, 'feb': 2, 'mar': 3}
months2 = {number: name for name, number in months.items()}
print(months2)

grades = {'ram': [98, 34, 56], 'Lucky': [56, 78, 90]}


grades2 = {k: sum(v)/len(v) for k, v in grades.items()}
print(grades2)
