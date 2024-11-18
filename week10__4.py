x, y = ["A", "B", "C", "D", "E", "F", "G", "H"], [1, 2, 3, 4, 5, 6, 7, 8]
chess = [f"{x[i]}{y[j]}" for i in range(8) for j in range(8) if (i%2 == 0 and j%2 ==0) or (i%2 != 0 and j%2 != 0)]
print(chess)
#test