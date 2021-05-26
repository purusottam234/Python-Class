

# + operator is used to Concatenate lists

list1 = [10, 20, 30]
list2 = [40, 50]
concatenated_list = list2 + list1
print(concatenated_list)

for i in range(len(concatenated_list)):
    print(f'{i}:{concatenated_list[i]}')
