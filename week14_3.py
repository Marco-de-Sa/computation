while True:
    n = int(input("give me a number: "))
    if n > 0:
        break

for i in range(n):
    for j in range(n):
        print(i+1, end= " ")
    print()