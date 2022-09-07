for i in range(10, 21):
    if i != 12 or i != 15 or i != 18:
        print(i)

for i in range(10, 21):
    if i == 12 or i == 15 or i == 18:
        continue
    else:
        print(i)
