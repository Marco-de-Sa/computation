gameCount, totalCost = int(input("how many games have you bought this month: ")), 0.0
for i in range(gameCount):
    totalCost += float(input(f"how much did game {i+1} cost?: "))
if totalCost > 100:
    print(f"you have issues, also the total cost is {totalCost}")
else:
    print(f"the total cost is {totalCost}")