l1, l2 = [2,3,4,6], [1,3,5,6]
commonL = []
for i in l1:
    if i in l2:
        commonL.append(i)
print(commonL)