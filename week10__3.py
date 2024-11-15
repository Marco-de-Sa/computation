x, y = ["A", "B", "C", "D", "E", "F", "G", "H"], [1, 2, 3, 4, 5, 6, 7, 8]
chess = [f"{x[i]}{y[j]}" for i in range(8) for j in range(8)]
print(chess)