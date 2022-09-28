data = [int(i) for i in input().split()]  # Молодец!
# data.sort(reverse=True)
# ind = 0
# if len(data) > 0:
#     print(data[0], data[-1])
# else:
#     print(None)

# 2
if len(data) > 0:
    print(max(data), min(data))
else:
    print(None)
