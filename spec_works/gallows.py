import random

print('Категории: \n1. animals\n2. fruits')
catalog = input(f'\nВыберите категорию: ')
animals = ['elifan', 'cat', 'dog']
fruits = ['apple', 'oring', 'banana']
death = 7
current_catalog = []
counter = 1

# выбор категории
if catalog == '1' or catalog == 'animals':
    current_catalog = animals
elif catalog == '2' or catalog == 'fruits':
    current_catalog = fruits

# рандомным образом выбирает слово из категории
random_word = random.randint(0, len(current_catalog)-1)
blink = list(current_catalog[random_word])

sq = ["*" for i in range(len(blink))]

# Основной блок кода
while death != 0 or blink != []:
    if death > 0 and len(blink) > 0:
        guessed = input(f'Введите {counter} букву из {len(blink)}: ')
        if guessed not in blink:
            death -= 1
            print(f'Вы не угадали букву и у вас осталось {death} жизней, попробуйте ввести букву еще раз!')
        elif guessed in blink:
            print(f'Вы угадали букву в слове, введите следующую')
            for i in blink:
                a = blink.index(i)
                if guessed == i:
                    sq[a] = blink[a]
                    blink.remove(i)
                    print(*sq)

            print()
    else:
        break

# Определяет победил пользователь или проиграл
if blink == []:
    print('Вы победили! слово:', *(current_catalog[random_word].split()))
else:
    print('Вы проиграли! и не угадали слово', *(current_catalog[random_word].split()))
