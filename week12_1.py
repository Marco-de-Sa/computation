def getSmall(list):
    temp = list[0]
    for i in range(len(list)):
        if temp > list[i]:
            temp = list[i]
    print(temp)

while True:
    x = input("how many numbers: ")
    if x.isdigit() and int(x) > 0:
        x = int(x)
        break
count = 0
numList = [int(input("input a number")) for i in range(x)]
getSmall(numList)