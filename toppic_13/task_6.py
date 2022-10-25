data = input("Ведите ваш текст: ").split()
f = []
print("Результат:", end=" ")
for i in data:
    if f.count(i) >= 1:
        print(f"{i}_{f.count(i)}", end=" ")
        f.append(i)
    else:
        print(i, end=" ")
        f.append(i)
