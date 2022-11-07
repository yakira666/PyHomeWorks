list_of_synonyms = dict([input("Введите слово и синоним(разделенные пробелами): ").title().split()
                         for _ in range(int(input("Введите колличество слов для добавления: ")))])

num_word = input("Введите искомое слово: ").capitalize()

if num_word in list_of_synonyms.values():
    for k in list_of_synonyms:
        if num_word == list_of_synonyms.get(k):
            print(k)
            break
if num_word in list_of_synonyms.keys():
    print(list_of_synonyms.get(num_word))
