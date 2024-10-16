n = input("input your name: ")
if n[-1]=="a":
    temp = n[0:len(n) - 1]
    n = temp + "inha"
elif n[-1]=="o":
    temp = n[0:len(n) - 1]
    n = temp + "inho"

print(f"{n} is a nice name :)")