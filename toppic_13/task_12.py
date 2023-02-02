key_count = {}
for word in input("Ведите ваш текст: ").lower().split():  # Еду еду в чистом поле

    # key_count[word] = key_count.get(word, -1) + 1
    # print(key_count.get(word), end=" ")
    key_count[word] = key_count.get(word, 0) + 1
    print(key_count.get(word) - 1, end=" ")
