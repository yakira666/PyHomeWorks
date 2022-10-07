data = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 5)]
data_2 = [[j for j in data[i]]for i in range(len(data))]
print(data_2)
