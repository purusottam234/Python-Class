import re
pattern = '454656'
a = "Match" if re.fullmatch(pattern, '454656') else "No match"
print(a)
print("valid" if re.fullmatch(r'\d{5}', '02215') else "invalid")
print("valid" if re.fullmatch("[A-Z][a-z]*", "Lucky")else "invalid")
print("valid" if re.fullmatch("[A-Z][a-z]+", "Lucky")else "invalid")


print("valid" if re.fullmatch('label?ed', 'labeled') else 'no match')

# replacing substrings and splitting strings

print(re.sub(r'\t', ', ', '1\t2\t3\t4'))
print(re.sub(r'\t', ', ', '1\t2\t3\t4', count=2))

# split
print(re.split(r',\s*', '1, 2, 3, 4,5, 6,7,8'))

# search

# result = re.search("hello", "Python is fun", flags=re.IGNORECASE)
# print(result.group() if result else "not result")

# ^
result = re.search("^Python", "Python is  fun")
print(result.group() if result else "not found")
