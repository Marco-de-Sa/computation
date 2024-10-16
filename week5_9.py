a, num, temp = input("say something about nova: "), 0, ""
arr = a.split(" ")
for x in arr:
    if "nova" in arr[num].lower():
        arr[num] = "Universidade Nova de Lisboa"
    elif "nova" not in a.lower():
        print("are you sure you are talking about nova?")
        break
    temp = temp + " " + arr[num]
    num += 1
print(temp.strip())