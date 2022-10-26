data = input().upper()

set_data = set(data)
frst_dict = dict()

for i in set_data:
    frst_dict.setdefault(i, data.count(i))
print(frst_dict)

# Отлично!

# Эту задачу нужно будет решить другим способом (используя генератор словарей),
# после того, как мы посмотрим генератор словарей
