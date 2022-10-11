"""
ЗАДАЧА:
Найдите размеры следующих множеств:
al_num = {'A', 1, 'B', 2, 'C', 3}
fruits = {'Kiwi', 'Orange', 'Coconut', 'Pineapple', 'Mandarin'}
browsers = {(1, 'Chrome'), (2, 'Yandex'), (3, 'Firefox'), (4, 'Opera')}
"""

al_num = {'A', 1, 'B', 2, 'C', 3}
fruits = {'Kiwi', 'Orange', 'Coconut', 'Pineapple', 'Mandarin'}
browsers = {(1, 'Chrome'), (2, 'Yandex'), (3, 'Firefox'), (4, 'Opera')}
print(
    f'Размер множества: al_num состовляет: {al_num.__sizeof__()} байт\n'
    f'Размер множества: fruits состовляет: {fruits.__sizeof__()} байт\n'
    f'Размер множества: browsers состовляет: {browsers.__sizeof__()} байт'
)
# Отлично!
