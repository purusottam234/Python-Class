roman_numericals = {'I': 1, "II": 2, "III": 3, "V": 5, "X": 100}
print(roman_numericals)

# print(roman_numericals['V'])

roman_numericals['X'] = 10
roman_numericals['L'] = '50'
# del statement delete a key value pair
del roman_numericals['I']

# pop can remove a key value pair

roman_numericals.pop("L")
# print(roman_numericals[

print("I" in roman_numericals)
print(roman_numericals)
