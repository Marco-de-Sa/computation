def list_sum(mat):
    tempArr = []
    for i in range(len(mat)):
        count = 0
        for j in range(len(mat[0])):
            count += mat[i][j]
        tempArr.append(count)
    tempVal = 0
    for i in tempArr:
        if tempVal < i:
            tempVal = i
    for i in range(len(tempArr)):
        if tempVal == tempArr[i]:
            print(mat[i])

y = int(input("input num of rows: "))
x = int(input("input number of columns: "))

matr = [[int(input("gimme a number")) for j in range(x)] for i in range(y)]

print(matr)
list_sum(matr)