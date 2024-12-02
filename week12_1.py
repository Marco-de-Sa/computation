# following function gets the smallest value in the parsed list
def get_small(list1):
    temp = list1[0]
    for i in range(len(list1)):
        if temp > list1[i]:
            temp = list1[i]
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
get_small(numList)