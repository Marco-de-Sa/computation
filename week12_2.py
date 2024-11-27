import math
def option_one():
    st = input("input a word")
    print(st.upper())
def option_two():
    colour = input("what is your favourite colour?")
    print(f"{colour} is a terrible choice")
def option_three():
    print(math.pi)
while True:
    x = int(input("choose 1, 2 or 3"))
    if x == 1:
        option_one()
        break
    if x == 2:
        option_two()
        break
    if x == 3:
        option_three()
        break