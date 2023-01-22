m = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [list(map(int, row)) for row in m]
tran = list(zip(*matrix))
print(tran, type(tran))

# multiplied = list(map(lambda a,b: a*b, m, tran))
# print(multiplied)
