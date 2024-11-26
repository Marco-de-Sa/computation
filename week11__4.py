length = int(input("how many numbers: "))
List = [int(input("input a number: ")) for i in range(length)]
choice = input(f"Choose from the following options:\nOption 1: Create a new list whose values are the original’s to the power of 2\nOption 2: Create a matrix with 3 lines, where the first is the original list, the second is the list with the values doubled, and the third line the list with tripled values.\nOption 3: Have the user insert a new list, and append it to the first.")
if choice == "1":
    for i in range(len(List)):
        List[i] **= 2
elif choice == "2":
    final = [List]
    for j in range(2):
        temp = List
        final.append(temp)
        for i in range(len(temp)):
            temp[i] *= (2+j)
    List = final
elif choice == "3":
    length = int(input("how many numbers: "))
    newList = [int(input("input a number: ")) for i in range(length)]
    List.append(newList)

print(List)