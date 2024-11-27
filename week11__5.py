x = [[f"{j+1} x {i+1} = {(i+1)*(j+1)}" for i in range(10)] for j in range(10)]
for i in range(len(x)):
    for j in range(len(x)):
        print(f"{x[i][j]}\t\t", end=" ")
    print()