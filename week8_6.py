my_list = [1,2,3]
add = 0
for i in my_list:
    add+=i

ave = add/len(my_list)

while ave <= 5:
    temp = int(input("input a integer to add to the list: "))
    my_list.append(temp)
    add+=temp
    ave = add / len(my_list)

# while sum(my_list)/len(my_list) <= 5:
#     my_list.append(int(input("input a integer to add to the list: ")))
#     print(f"the numbers are:{my_list}\nand the average is {sum(my_list)/len(my_list)}")