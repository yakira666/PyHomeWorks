contacts = {}
rec_list = [input("Введите слово и синоним(разделенные пробелами): ").title().split() for _ in
            range(int(input("Введите количество записей: ")))]

for i in rec_list:
    contacts[i[0]] = contacts.get(i[0], [])
    contacts.get(i[0]).append(i[1])

for i in range(int(input("Введите количество искомых абонентов: "))):
    s = input("Введите имя абонента: ").strip().title()
    print(*(contacts.get(s, "абонент не найден..")))
