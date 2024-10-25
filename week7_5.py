intList, count, listSize = [], 0, int(input("input the size of the list: "))
for i in range(0, listSize):
    intList.append(int(input("input an integer: ")))

for i in range(len(intList)):
    if intList[i]%2 == 0:
        count += 1
print(f"the list that was given is:\n{intList}\n")
print(f"There are {count} even integer values in the list")