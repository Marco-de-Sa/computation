# takes two ints and puts a to the power of b afterward it returns the result
def to_power(a, b):
    return a**b

# asks for two numbers, parses them into to_power and then prints out the returned value
print(to_power(int(input("input first num: ")), int(input("input second num: "))))