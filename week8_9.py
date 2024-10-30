a = input("input a string: ")
for i in range(len(a)):
    if a[i]==a[i].upper() and a[i]!=a[i].lower():
        print("capital letter detected!")
        break