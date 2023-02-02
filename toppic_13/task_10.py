import time

synonyms = dict([input("Введите слово и синоним(разделенные пробелами): ").title().split()
                 for _ in range(int(input("Введите колличество слов для добавления: ")))])

word = input("Введите искомое слово: ").capitalize()

start_2 = time.time()
for key, value in synonyms.items():
    if key == word:
        print(value)
    if value == word:
        print(key)
end_2 = time.time()

# ==================================================================

start_1 = time.time()
if word in synonyms.values():
    for k in synonyms:
        if word == synonyms.get(k):
            print(k)
            break

if word in synonyms.keys():
    print(synonyms.get(word))
end_1 = time.time()

print(f'{end_1 - start_1:.12f}')
print(f'{end_2 - start_2:.12f}')
