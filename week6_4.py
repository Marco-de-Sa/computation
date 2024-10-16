numArr= []
for i in range(1, 101):
    numArr.append(i)
    if numArr[i-1]%10==0:
        print(f"that is 10 numbers printed {numArr[i-1]}")