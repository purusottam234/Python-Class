months = {'january': 31, 'february': 30, 'march': 31}

# for month_name in months.keys():
#     print(month_name, end=" ")

# for month_name in months.values():
#     print(month_name, end=" ")


month_view = months.keys()
for key in month_view:
    print(key, end=" ")

months["December"] = 23
print(months)

for key in month_view:
    print(key, end=" ")
