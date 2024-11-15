intList = [int(input("input a number: ")) for i in range(4)]
temp = intList[0]
for i in range(len(intList)):
    if temp < intList[i]:
        temp = intList[i]
print(temp)