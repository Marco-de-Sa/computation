a, b = float(input("input the first number")), int(input("input the second number"))
temp = a
for i in range(b-1):
    a*=temp
print(a)