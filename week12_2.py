import math

# asks for a word and puts it into uppercase when it is called
def option_one():
    st = input("input a word")
    print(st.upper())
# asks what your favourite colour is and mocks it when it is called
def option_two():
    colour = input("what is your favourite colour?")
    print(f"{colour} is a terrible choice")
# prints out pi using the math class when it is called
def option_three():
    print(math.pi)

# a while loop that will forever repeat unless one of the internal if statements are met
while True:
    x = int(input("choose 1, 2 or 3"))
    # if the inputted value is 1 calls the option_one function and then breaks out of the while loop afterward
    if x == 1:
        option_one()
        break
    # if the inputted value is 1 calls the option_two function and then breaks out of the while loop afterward
    elif x == 2:
        option_two()
        break
    # if the inputted value is 1 calls the option_three function and then breaks out of the while loop afterward
    elif x == 3:
        option_three()
        break