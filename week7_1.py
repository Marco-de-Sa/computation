itemAmount, itemList = int(input("how many items are you going to buy")), []
for i in range(itemAmount):
    itemList.append(input(f"input {i + 1} item in list"))
print("\n\nShopping item list:")
for i in range(itemAmount):
    print(f"{i+1}.\t{itemList[i]}")