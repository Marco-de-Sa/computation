lMat = [[5, 4], [3, 5], [1, 2], [0, 0]]
print(f"{lMat[1][0]}, {lMat[2][1]}")
print(f"{lMat[0][0]}+{lMat[0][-1]}+{lMat[-1][0]}+{lMat[-1][-1]} = {lMat[0][0]+lMat[0][-1]+lMat[-1][0]+lMat[-1][-1]}")
print(f"columns: {len(lMat[0])}\nRows: {len(lMat)}")
bigger3 = 0
for i in range(len(lMat)):
    for j in lMat[i]:
        if j > 3:
            bigger3 += 1
print(f"{bigger3} numbers are bigger than 3")