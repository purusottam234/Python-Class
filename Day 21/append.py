def Simappend(sentences):
    output = []
    for word in sentences.split():
        if word[0] in 'aeiou':
            output.append(f'{word} way')
        else:
            output.append(f'{word[1:]}{word[0]} ay')
    return " ".join(output)


print(Simappend("this is the test sample"))
