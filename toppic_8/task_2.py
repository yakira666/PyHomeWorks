for i in range(10, 21):
    if i == 12 or i == 15 or i == 18:
        continue
    print(i)
print()


# Решение без else
for i in range(10, 21):
    if i % 3 == 0:
        continue
    print(i)
