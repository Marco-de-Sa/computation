def match_list(L1, L2):
    templist = []
    for i in range(len(L1)):
        templist.append(f"{L1[i]} {L2[i]}")
    return templist
groupNum = int(input("how many people are in the group: "))
groupFirstName = [input(f"first name of group member {i}: ") for i in range(groupNum)]
groupJobName = [input(f"job name of group member {i}: ") for i in range(groupNum)]
print(match_list(groupFirstName, groupJobName))