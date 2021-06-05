def Simple(word):
    if word[0] in "aeiou":
        return f'{word} way'
    return f'{word[1:]}{word[0]} ay'


print(Simple("Python"))
