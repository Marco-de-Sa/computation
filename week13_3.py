x = input("input a list of numbers separated by a comma and a space: ")
x = x.split(", ")
l = []
for i in range(len(x)):
    l.append(int(x[i]))
print(l)
for i in range(len(l)):
    l[i]+=10
print(l)