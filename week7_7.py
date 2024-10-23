gameCount, totalCost, gameNames,temp = int(input("how many games have you bought this month: ")), 0.0, [],0
for i in range(gameCount):
    totalCost += float(input(f"how much did game {i+1} cost?: "))
for i in range(gameCount):
    gameNames.append(input(f"input the name of game number {i + 1}: "))
for i in range(len(gameNames)):
    if "assassin's creed" in gameNames[i].lower():
        temp+=1
if totalCost > 100:
    print("you have issues")
print(f"there are {temp} Assassin's creed games in the list")