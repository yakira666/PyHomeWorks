data = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# # №1
# data_2 = []
# for i in range(len(data)):
#     if data[i] != ():
#         data_2.append(data[i])
# print(data_2)

# №2 ДОДЕЛАТЬ НА ИНПУТ
data = [i for i in input().strip("[]").replace("(", "").replace(")", "").replace(",", "").replace("\'","").replace("\'", "").replace(" ", "")]
print(data)

# №3
