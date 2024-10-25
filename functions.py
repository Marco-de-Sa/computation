# defines a function
def addition(num1, num2):
    # additions the two args together then additions assigns it to the temp variable
    temp = num1 + num2

    # prints the temp value
    print(temp)

    # checks if the temp value is below 10 and if it is it calls the addition function again
    if temp <= 10:
        addition(temp, temp)

    # returns the string "numbers additioned successfully :)"
    return "numbers additioned successfully :)"

# prints the returned value off the addition function where arg 1 is 1 and arg 2 is 1
print(addition(1,1))