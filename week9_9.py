numL = []
for i in range(4):
    numL.append(int(input("input a number: ")))
for i in range(len(numL)):
    if numL[i]>600:
        print("high")
        break