my_List = [1, 22, 3, 44]
temp = 0
my_List[0]=100
for i in range(len(my_List)):
    if my_List[i] > 6:
        temp += my_List[i]
print(my_List)
print(temp)