x = input("input a list of numbers separated by a comma and a space: ")
x = x.split(", ")
for i in range(len(x)):
    x[i] = int(x[i])
