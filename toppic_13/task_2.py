data = input().upper()
print({k: data.count(k) for k in set(data)})
