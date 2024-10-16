# x, count = input("input a string: "), 0
# for i in range(len(x)):
#     if x[i] == " ":
#         count += 1
# print(count)
# if count == 0:
#     print("there are no spaces in the string")

# str=input("string gimme now! ")
# temp = ""
# count=0
# for i in range(len(str)):
#     count = -1-i
#     temp = temp + str[count]
# print(temp)

for i in range(1, 101, 1):
    if i%3 == 0:
        print(i, end=" ")