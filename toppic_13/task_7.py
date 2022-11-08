quantity = int(input("Введите колличество слов для добавления: "))

list_of_all_items = [input("Введите слово и описание(разделенные двоеточием): ").lower().split(":") for _ in
                     range(quantity)]

slang = {item[0].strip(): item[1].strip().capitalize() for item in list_of_all_items}

print(f"\nПолучите подробное описание сленговых слов")

list_search_values = [input("Введите слово: ").lower() for _ in range(int(input("Введите колличество искомых слов: ")))]

for k in list_search_values:
    print(f'{k.capitalize()} - {slang.get(k, "не найдено...")}')
