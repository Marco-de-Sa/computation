# try:
#     def greet(hello, world):
#         print(f"{hello} {world}")
#         x = range(10)[6]
#         print(x)
#         return 5**2
#
#     print(greet("hey", "john"))
#     try:
#         print(5/0)
#     except ZeroDivisionError:
#         print("sorry you cannot divide by zero")
#     # print(5/0)
#     try:
#         int(input("don't input an integer :)\n"))
#     except ValueError:
#         print("good job")
# except KeyboardInterrupt:
#     print("goodbye")

# text = input("Write a sequence of numbers, space(s) separated: ")
# list_of_strings = text.split()
# L = [float(element) for element in list_of_strings]
# count = 0
# for element in L:
#     if 10 <= element <= 20:
#         count += 1
# print(f"The list you entered contains {count} numbers in [10, 20]")

M = [[1, 3, 2],[4, 6, 7]]
soma = 0
for i in range(len(M)):
    for j in range(len(M[i])):
        soma+=M[i][j]
print(soma)