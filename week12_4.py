def determinate(matrix_func):
    x = matrix_func[0][0]*matrix_func[1][1] - matrix_func[0][1] * matrix_func[1][0]
    return x

matrix = [[int(input("input a number")) for i in range(2)] for j in range(2)]
print(matrix)
print(determinate(matrix))