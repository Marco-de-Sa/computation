rows = int(input("how many rows: "))
columns = int(input("how many columns: "))
Matrix = [[int(input("input a num: ")) for i in range(columns)] for j in range(rows)]
print(Matrix)