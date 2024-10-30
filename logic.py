# a=2
# b=-4.0
# c=-3
# d=20.0
# e=3
# flag1=True
# flag2=a==c
# f=20
#
# x=a!=e and flag2
# print(x)
#
# x=flag1 or flag2
# print(x)
#
# x=f/2 == a and flag2 or c-b != 1
# print(x)
#
# x=-2<-4 and not(2!=3 or 20 < 6*5-4)
# print(x)
#
# x=False and (b>c and flag2 or flag1)
# print(x)
#
# x=flag1 or (2+4*b-5 < f*3 and not(flag2))
# print(x)
#
# x=not(flag1) or not(flag2)
# print(x)


#define the variables
a = int(input("input the first value: "))
b = int(input("input the second value: "))

#the logical operations
temp = b == 74 or (a >= 3 * b and a % 3 == 0 and a % 2 == 0)

#if else statement to give an output based on the logical operation
if temp:
    print(f"the computer is happy because {temp}")
else:
    print(f"the computer is not happy because {temp}")