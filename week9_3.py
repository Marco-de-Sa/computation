name, count = [], 0
for i in range(5):
    name.append(input("input a name:"))
for i in range(len(name)):
    temp = name[i]
    if temp[0].lower() == "a":
        count+=1
print(count)