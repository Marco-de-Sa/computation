a = input("input a string: ")
for i in range(len(a)):
    if a[i]==a[i].upper() and a[i]!=" ":
        print("capital letter detected!")
        break