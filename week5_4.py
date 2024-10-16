x, y, c = int(input("insert the first int")), int(input("input the second value")), int(input("input a 1 if you want to see the result of multiplying their two numbers\ninput a 2 if you want the addition\nfinally input a 3 if you want to see the result of a to the power of b"))

if c==1:
    print(x + y)
elif c==2:
    print(x * y)
elif c==3:
    print(x**y)