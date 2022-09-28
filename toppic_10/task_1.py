# №1
# data = [15, 82, 30, 44, 10]
# if len(data) == 0:
#     print("Пустой список")
# elif len(data):
#     for i in range(len(data)):
#         print(f'{data[i]} {i}')

# №2
# if (len(data := [15, 82, 30, 44, 10])) == 0:
#     print("Пустой список")
# elif len(data):
#     for i in range(len(data)):
#         print(f'{data[i]} {i}')

# №3
if (len(data := [int(i) for i in input().split()])) == 0:
    print("Пустой список")
elif len(data):
    for i in data:
        print(f'{i} {data.index(i)}')
