# M = [[1, 2], [3,4], [5,6], [7,8]]
# for i in range(len(M)):
#     print(M[i])
    # for j in range(len(M[i])):
    #     print(M[i][j])

# y = int(input("input num of rows: "))
# x = int(input("input number of columns: "))
# M = [[0 for j in range(x)]for i in range(y)]
# print(M)
# for i in range(len(M)):
#     print(M[i])
# for i in range(len(M)):
#     for j in range(len(M[i])):
#         if i == j:
#             M[i][j] = int(input(f"input a value for pos ({i},{j})"))
# for i in range(len(M)):
#     print(M[i])

# N = int(input("how many rows and columns: "))
# M = [[float(input(f"input a value for ({j+1}, {i+1}): ")) for j in range(N)]for i in range(N)]
# count = 0
# for i in range(len(M)):
#     print(f"({M[i][i]})")
# for i in range(N-1):
#     print(M[i], end=", ")
# print(M[len(M)-1], end=";")
# for i in range(len(M)):
#     for j in range(len(M[i])):
#         if M[i][j] == 0:
#             print(f"zero detected at: ({i+1}, {j+1})")
#             count+=1
# if count > 0:
#     print(f"0 appears {count} times")
# else:
#     print("0 does not appear in the matrix")