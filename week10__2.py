groupNum = int(input("how many people are in the group: "))
groupFirstName = [input(f"first name of group member {i+1}: ") for i in range(groupNum)]
groupJobName = [input(f"job name of group member {i+1}: ") for i in range(groupNum)]
templist = []
for i in range(len(groupFirstName)):
    templist.append(f"{groupFirstName[i]}, {groupJobName[i]}")
print(templist)