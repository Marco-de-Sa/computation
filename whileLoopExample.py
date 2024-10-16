from random import randint

i = 1
x = 0
n =int(input("input the amount of times you would like to print?")) + 1
while i < n:
    print(i)
    i += 1
    x = int(input("input a 2, 1 or 0: "))
    if x == 1:
        print("you have continued")
        continue
    elif x ==0:
        print("ending while loop")
        break
    print("after :)")

s= [1,2,3,4,5,6,7,8,9]

for x in s:
    print(f"count: {x}")

p = randint(0, 10)

print(p)

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("sorry that results in an error")
