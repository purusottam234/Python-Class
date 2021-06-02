# split
letters = "A,B,C,D"

print(letters.split(","))
print(letters.split(",", 2))
# joining

# join

letters_list = ['A', 'B', 'C', 'D']
print(','.join(letters_list))
print(','.join([str(i) for i in range(10)]))

# partition splits a string into a tuple of three strings based on the method's seperator argument

# the part of the orginal string before the seperator
# the seperator itself
# the part of the string after seperator
print('Lucky:87, 34, 56'.partition(": "))

# split lines

lines = """
this is the line 1 
this is the line 2
this is the line end
"""
print(lines)
print(lines.splitlines())

# isdigit return true if the string on the method only contains the digit characters

print('-24'.isdigit())

# rawstring

file_path = "C:\\Users\\Purusottam\\Desktop\\My Personal\\SE\\slides"
print(file_path)
