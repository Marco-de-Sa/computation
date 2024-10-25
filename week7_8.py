numChild, childList, letters = int(input("how many children would you like to have?: ")), [],0
for i in range(numChild):
    childList.append(input(f"name of child number {i+1}: "))
for i in range(len(childList)):
    print(f"{len(childList[i])} letters are in {childList[i]}")
    letters += len(childList[i])