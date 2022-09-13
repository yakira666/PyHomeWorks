# data = input("Введите любую строку: ").split()
# # №1
# if len(data) == 1:
#     print("Строка состоит из одного слова")
# elif len(data) == 0:
#     print("Строка пустая")
# elif len(data) > 1:
#     print("В строке", "\"" + " ".join(data) + "\"", "-", len(data), "слов")

# Думаю, что пришло время начать использовать моржа :)

# №2
# if len(data := input("Введите любую строку: ").split()) == 0:
#     print("Строка пустая")
# elif len(data) > 0:
#     if len(data) == 1:
#         print("Строка состоит из одного слова")
#     else:
#         print("В строке", "\"" + " ".join(data) + "\"", "-", len(data), "слов")

# №3
print("Строка пустая") if len(data := input("Введите любую строку: ").split()) == 0 else \
    print("Строка состоит из одного слова") if len(data) == 1 \
    else print("В строке", "\"" + " ".join(data) + "\"", "-", len(data), "слов")
