data_str = input("Введите строку: ")
data_char = input("Введите букву: ")

# first = data_str.find(data_char)
first = data_str.index(data_char)
# last = data_str.rfind(data_char) + 1
last = data_str.rindex(data_char) + 1

print(data_str[:first] + data_str[last:])

'''
Отлично!
Логика задачи построена правильно, только метод был неправильным

Объясню, почему find() и rfind() более опасны, когда вводится буква, которой нет в строке, твоя программа
выведет неверные данные, но если ты используешь index() и rindex(), они вызовут ошибку ValueError, означающую, 
что буква не найдена в строке.

    Пример когда используется find() rfind():
Введите строку: In the hole in the ground there lived a hobbit
Введите букву: h
Результат: In tobbit

Введите строку: In the hole in the ground there lived a hobbit
Введите букву: f
Результат: In the hole in the ground there lived a hobbiIn the hole in the ground there lived a hobbit


    Пример когда используется index() rindex():
Введите строку: In the hole in the ground there lived a hobbit
Введите букву: h
Результат: In tobbit

Введите строку: In the hole in the ground there lived a hobbit
Введите букву: f
Результат: first = data_str.index(data_char) ValueError: substring not found
'''
