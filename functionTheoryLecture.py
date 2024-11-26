# def my_function():
#     print("hello world")
# my_function()

# def add(a, b):
#     return a + b
# x=2
# z = add(x, x)
# print(z)

# def repeat_text(s, n):
#     print(f"{s}\n"*n, end= "")
# repeat_text("hey guys!", 5)

# def plus_4(n):
#     """adds 4 to the parsed integer"""
#     n+=4
#     return n
# print(plus_4(4))
# print(plus_4(4).__doc__)

# complex data types that are parsed into the function don't need to be returned because the value on the
# parameters and the value of the parsed complex datatype are addressed to the same pointer

# def plus_4_arr(v):
#     v[0]+=4
#     v[1]+=4
# vet = [10, 15]
# plus_4_arr(vet)
# print(vet)
# this'll print out 14 and 19