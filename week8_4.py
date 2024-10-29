ltNum, howManyNum, i = [], int(input("how many numbers do you want to input: ")), 0
while i <howManyNum:
    ltNum.append(int(input("input an integer: ")))
    i+=1
for i in range(len(ltNum)):
    if ltNum[i]%2==0:
        print(f"{ltNum[i]} is an even number")
    else:
        print(f"{ltNum[i]} is an odd number")