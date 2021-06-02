# count
sentence = "hsgjahgksahihuieuriuhcxjkjhzoivhdsioh"
a = sentence.count('j')
print(a)
# index
b = sentence.index('j')
print(b)

# rindex
c = sentence.rindex('j')
print(c)

# find and rfind acts as index and rindex method

# determine whether a string contains a substring

print("a" in sentence)
print("a" not in sentence)

#startwith and endswith
print(sentence.startswith('hs'))
print(sentence.endswith('hs'))


# replacing substring

values = '1\t2\t3\t4\t5'
print(values.replace("\t", ","))
