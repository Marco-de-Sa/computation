intList, count = [], 0
for i in range(5):
    intList.append(int(input("input an integer: ")))

for i in range(len(intList)):
    if intList[i]%2 == 0:
        count += 1
print(f"the list that was given is:\n{intList}\n")
print(f"There are {count} even integer values in the list")