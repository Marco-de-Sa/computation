a = input("input a password: ")
upperCount = 0
while upperCount<2:
    for i in range(len(a)):
        if a[i]==a[i].upper() and a[i]!=a[i].lower():
            upperCount+=1
            if upperCount >= 2:
                print("password accepted!")
                break
    if upperCount<2:
        a = input("please only input a valid password: ")