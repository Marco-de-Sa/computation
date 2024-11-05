def greet(hello, world):
    print(f"{hello} {world}")
    x = range(10)
    print(x)
    return 5**2

print(greet("hey", "john"))
try:
    print(5/0)
except ZeroDivisionError:
    print("sorry you cannot divide by zero")
# print(5/0)
try:
    int(input("don't input a number :)"))
except ValueError:
    print("good job")
