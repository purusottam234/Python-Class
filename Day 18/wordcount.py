from collections import Counter
text = ('this is the sample text with different words'
        'this is the sample text with different words')


# word_counts = {}

# for word in text.split():
#     if word in word_counts:
#         word_counts[word] += 1
#     else:
#         word_counts[word] = 1

# print(f' {"WORD":<12} COUNT')
# for word, count in sorted(word_counts.items()):

#     print(f'{word:<12}{count}')
# print("\nNumber of unique words:", len(word_counts))


counter = Counter(text.split())
for word, count in sorted(counter.items()):
    print(f'{word:<12} {count}')
