import random

print('Категории: \n1. animals\n2. fruits')
catalog = input(f'\nВыберите категорию: ')
animals = ['elephant', 'cat', 'dog']
fruits = ['apple', 'oring', 'banana']
current_catalog = []

# выбор категории
if catalog == '1' or catalog == 'animals':
    current_catalog = animals
elif catalog == '2' or catalog == 'fruits':
    current_catalog = fruits

# рандомным образом выбирает слово из категории
word = random.choice(current_catalog)
blink = list(word)

sq = list("_" * len(blink))

counter = 1
death = 7
# Основной блок кода
while ("".join(sq) != word) or (death < 0):
    guessed = input(f'Введите {counter} букву из {len(blink)}: ')
    if guessed not in blink:
        death -= 1
        print(f'Вы не угадали букву и у вас осталось {death} жизней, попробуйте ввести букву еще раз!')
    elif guessed in blink:

        a = blink.index(guessed)
        sq[a], blink[a] = blink[a], sq[a]
        print("".join(sq))
        print(f'Вы угадали букву в слове, введите следующую')
        counter += 1

# Определяет победил пользователь или проиграл
if (res := "".join(sq)) == word:
    print('Вы победили! слово:', res)
else:
    print('Вы проиграли! и не угадали слово', res)
