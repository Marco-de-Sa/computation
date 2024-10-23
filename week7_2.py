from random import randint
exList = []

for i in range(20):
    exList.append(randint(1,10))

for i in range(len(exList)):
    if i%2!=0:
        exList[i] = exList[i]*2
    else:
        exList[i] = exList[i]*3

print(exList)