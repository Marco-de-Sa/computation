# following function gets the smallest value in the parsed list
def getSmall(list):
    temp = list[0]
    for i in range(len(list)):
        if temp > list[i]:
            temp = list[i]
    print(temp)

# following while loop keeps iterating until a number above 0 is inputted
while True:
    x = input("how many numbers: ")
    if x.isdigit() and int(x) > 0:
        x = int(x)
        break
count = 0

# this is the comprehension list we will use for the earlier getSmall function
numList = [int(input("input a number")) for i in range(x)]

# calls getSmall with numList as the parsed list
getSmall(numList)