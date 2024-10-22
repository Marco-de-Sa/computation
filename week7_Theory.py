name, SD, classNum, classRef = input("input your name: "), input("input your student number: "), int(input("how many classes do you have?: ")), []
scholarships = ["20221111", "20222222", "20223333", "20224444", "20219999", "20218888", "20214444"]
for i in range(classNum):
    classRef.append(input("class reference: "))
price = []
costFinal=0
for i in range(classNum):
    if classRef[i][-3] == "I" and classRef[i][-2] == "I":
        price.append(150)
    elif classRef[i][-2] == "I":
        price.append(120)
    elif classRef[i][-1] == "I":
        price.append(100)
if SD in scholarships:
    for i in range(len(price)):
        price[i] = float(price[i])*(1-0.15)
print("------------------------------------------------------")
print(f"Name: {name}\nstudent number: {SD}\nNumber of classes: {classNum}\nList of classes:")
for i in range(classNum):
    print(f"- {classRef[i]}")
print(f"cost list: {price}")
for i in range(len(price)):
    costFinal+= price[i]
print(f"the final price is: {costFinal}")