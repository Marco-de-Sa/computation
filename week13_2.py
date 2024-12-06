def get_even(xList):
    tempList = []
    for i in xList:
        if i % 2 == 0:
            tempList.append(i)
    return tempList
listLen = int(input("input the length of the list you are making: "))
x = [int(input("input a value: ")) for i in range(listLen)]
print(get_even(x))