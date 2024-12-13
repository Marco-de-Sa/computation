M = [[99,88,77],[66,55,44],[33,22,11]]

for i in range(len(M)):
    som_van = 0
    for j in range(len(M[i])):
        som_van+=j
        M[i][j] = som_van
print(M)