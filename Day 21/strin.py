def Sentence(word):
    output = []
    for letter in word:
        if letter in 'aeiou':
            output.append(f'hi{letter}')

        else:
            output.append(letter)

    return ''.join(output)


print(Sentence("python"))
