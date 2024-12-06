def ave_mat(mat):
    som_van = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            som_van += mat[i][j]
    return som_van/(len(mat[0])*len(mat))
def large_mat(mat):
    temp = mat[0][0]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] > temp:
                temp = mat[i][j]
    return temp


y = int(input("input num of rows: "))
x = int(input("input number of columns: "))
matr = [[int(input("gimme a number")) for j in range(x)] for i in range(y)]
print(ave_mat(matr))
print(large_mat(matr))