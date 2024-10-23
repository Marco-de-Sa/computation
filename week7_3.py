nameAmount, nameList = int(input("how many names do you have: ")), []
for i in range(nameAmount):
    nameList.append(input(f"input name number {i + 1}: "))
print(nameList)
print(f"{nameList[0]} {nameList[len(nameList)//2]} {nameList[-1]}")
