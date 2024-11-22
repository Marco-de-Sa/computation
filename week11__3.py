M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
newM = []
som = 0
for i in range(len(M)):
    for j in range(len(M[i])):
        som+= M[i][j]
print(som)
print(M[-1])
for i in range(len(M)):
    for j in range(len(M[i])):
        if i == j:
            newM.append(M[i][j])
print(newM)