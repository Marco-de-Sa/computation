# takes a list that is presumably in the form of a 2x2 matrix and calculates the determinate
def determinate(matrix_func):
    x = matrix_func[0][0]*matrix_func[1][1] - matrix_func[0][1] * matrix_func[1][0]
    return x

# creates a 2x2 matrix
matrix = [[int(input("input a number")) for i in range(2)] for j in range(2)]
# prints the matrix
print(matrix)
# parses the matrix into the determinate function
print(determinate(matrix))