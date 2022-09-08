# я согласен с этим решением, нам нужно решить задачу используя оператор continue
for i in range(10, 21):
    if i != 12 and i != 15 and i != 18:
        print(i)
print()
# это реализовано неправильно, зачем нам блок else в if?
for i in range(10, 21):
    if i == 12 or i == 15 or i == 18:
        continue
    else:
        print(i)
print()

# эту задачу можно оптимизировать, конечно это хитрое решение, но более эффективное, чем i == 12 или i == 15 или == 18

for i in range(10, 21):
    if i % 3 == 0:
        continue
    else:
        print(i)