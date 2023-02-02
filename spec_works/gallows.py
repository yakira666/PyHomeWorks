import random

print('Категории: \n1. animals\n2. fruits')
cat_num = int(input(f'\nВыберите категорию: '))
catalogs = {
    1: ['elephant', 'cat', 'dog'],
    2: ['apple', 'oring', 'banana'],
}

# выбор категории
if not catalogs.get(cat_num):
    print('Выберите цифру из каталога')
else:
    current_catalog = catalogs.get(cat_num)
    # рандомным образом выбирает слово из категории
    word = random.choice(current_catalog)
    blink = list(word)

    sq = list("_" * len(blink))

    counter = 1
    death = 7
    print(f'\nДлина загаданного слова {len(blink)}\n')
    # Основной блок кода
    while ("".join(sq) != word) or (death < 0):
        guessed = input(f'Введите букву: ').lower()
        if guessed not in blink:
            death -= 1
            print(f'Вы не угадали букву и у вас осталось {death} жизней.')
        elif guessed in blink:

            a = blink.index(guessed)
            sq[a], blink[a] = blink[a], sq[a]
            print("".join(sq))
            counter += 1

    # Определяет победил пользователь или проиграл
    if (res := "".join(sq)) == word:
        print('Вы победили! слово:', res)
    else:
        print('Вы проиграли! и не угадали слово', res)

