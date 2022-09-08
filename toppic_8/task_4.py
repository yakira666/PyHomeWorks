list_nums = [21, 85, 150, 190, 135, 515, 80]

for i in list_nums:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        print(i)
# Отлично!
