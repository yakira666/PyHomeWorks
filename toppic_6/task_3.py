num = int(input("Введите целое число: "))

# Если положительно то 1, если отрицательное -1, если 0 то 0
# if num < 0:
#     print(-1)
# elif num > 0:
#     print(1)
# else:
#     print(0)  # Отлично!

print(-1) if num < 0 else print(1) if num > 0 else print(0)
