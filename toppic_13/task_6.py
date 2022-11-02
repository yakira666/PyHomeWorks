data = input("Ведите ваш текст: ").split()
s = {}

print("Результат:", end=" ")
for i in data:
    if i not in s:
        s.setdefault(i)
        print(i, end=" ")
        s[i] = 0
    else:
        s[i] += 1
        print(f"{i}_{s[i]}", end=" ")
