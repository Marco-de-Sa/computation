# defines a function
def add(num1, num2):
    # adds the two args together then adds assigns it to the temp variable
    temp = num1 + num2
    # prints the temp value
    print(temp)
    # checks if the temp value is below 10 and if it is it calls the add function again
    if temp <= 10:
        add(temp, temp)
    # returns the string "numbers added successfully :)"
    return "numbers added successfully :)"
print(add(1,1))