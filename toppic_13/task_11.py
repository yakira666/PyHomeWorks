contacts = {}

records = [input("Введите имя и телефон: ").title().split() for _ in
           range(int(input("Введите количество записей: ")))]

for name, phone in records:
    contacts[name] = contacts.get(name, []) + [phone]

for i in range(int(input("Введите количество искомых абонентов: "))):
    name = input("Введите имя абонента: ").strip().title()
    print(*(contacts.get(name, ["аобнент не найден.."])))
