def add(num1, num2):
    temp = num1 + num2
    print(temp)
    if temp <= 10:
        add(temp, temp)
    return "numbers added successfully :)"
print(add(1,1))