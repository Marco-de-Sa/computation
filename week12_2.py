import math

def optionOne():
    st = input("input a word")
    print(st.upper())
def optionTwo():
    colour = input("what is your favourite colour?")
    print(f"{colour} is a terrible choice")
def optionThree():
    print(math.pi)
while True:
    x = int(input("choose 1, 2 or 3"))
    if x == 1:
        optionOne()
        break
    if x == 2:
        optionTwo()
        break
    if x == 3:
        optionThree()
        break