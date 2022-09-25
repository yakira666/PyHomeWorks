data = [int(i) for i in input().split()]
data.sort(reverse=True)
ind = 0
if len(data) > 0:
    print(data[0], data[-1])
else:
    print(None)
