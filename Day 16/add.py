# add and remove elements

color_names = ['orange', 'yellow', 'green']
# insert method
color_names.insert(0, 'red')
print(color_names)

# append to insert in end

color_names.append("blue")
print(color_names)

# extend add all the elements of another sequence to end of a list

color_names.extend(['violet', 'indigo'])
print(color_names)
# extend method is equal to +=

sample_list = []
s = 'abc'
sample_list.extend(s)
print(sample_list)
t = (1, 2, 3)
sample_list.extend(t)
print(sample_list)

sample_list.extend((4, 5, 6))
print(sample_list)
# delete

# remove method delete the specify element with a specified value
color_names.remove('green')
print(color_names)

# clear method deletes all the elements\
# equivalent with slice assignment color_names[:]

color_names.clear()
print(color_names)
print(color_names[:])
