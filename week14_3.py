n = input("give me a number: ")
while not(n.isdigit()) or n == "0":
    n = input("give me a number: ")

n = int(n)

for i in range(n):
    for j in range(n):
        print(i+1, end= " ")
    print()