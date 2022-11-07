key_count, for_count = {}, []
for word in input("Ведите ваш текст: ").split():
    for_count.append(word)
    key_count[word] = key_count.get(word, 0)
    print(key_count.get(word), end=" ")
    key_count[word] = for_count.count(word)
