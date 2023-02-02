counter, temp = {}, []
for ch in input("Ведите ваш текст: ").split():
    if ch not in temp:
        temp.append(ch)
    else:
        counter[ch] = counter.get(ch, 0) + 1
        print(counter)
        temp.append(f"{ch}_{counter.get(ch)}")
        print(temp)

# ======================================================
# data = input("Ведите ваш текст: ").split()
# s = {}
#
# print("Результат:", end=" ")
# for i in data:
#     if i not in s:
#         s.setdefault(i, 0)
#         print(i, end=" ")
#     else:
#         s[i] += 1
#         print(f"{i}_{s[i]}", end=" ")
