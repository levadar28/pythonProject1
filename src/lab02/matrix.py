def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat) == 0:
        return []
    rowlenght = len(mat[0])
    for row in mat:
        if len(row) != rowlenght:
            raise ValueError
    return [[row[index] for row in mat] for index in range(rowlenght)]
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([[]]))
print(transpose([[1, 2], [3]]))







#def row_sums(mat: list[list[float | int]]) -> list[float]:
#    if len(mat) == 0:
 #       return []
#    rowlenght = len(mat[0])
#    for row in mat:
#        if len(row) != rowlenght:
#            raise ValueError
#    return [sum(row) for row in mat]
#print(row_sums([[1, 2, 3], [4, 5, 6]]))
#print(row_sums([[-1, 1], [10, -10]]))
#print(row_sums([[0, 0], [0, 0]]))
#print(row_sums([[1, 2], [3]]))








def transpose(mat: list[list[float | int]]) -> list[list[float | int]]:
    if len(mat) == 0:
        return []
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

def col_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat) == 0:
        return []
    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("Все строки матрицы должны иметь одинаковую длину")
    newmat = transpose(mat)
    return [sum(row) for row in newmat]
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))























