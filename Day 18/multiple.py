# multiple keys can contains same values
day_per_month = {'january': 31, 'february': 30, 'march': 31}
print(day_per_month)

for month, days in day_per_month.items():
    print(f'{month} has {days} days')
