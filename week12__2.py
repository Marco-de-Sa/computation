# takes a list and a variable then it returns the indexes where the variable is found in
def var_in_list(arr, var):
    positions = []
    for i in range(len(arr)):
        if arr[i] == var:
            positions.append(i)
    print(f"{var} appears in indexes {positions}")

# defines a pre-made list and variable and parses it into the var_in_list function
num = int(input("input a the length of a list: "))
l = [int(input("input a number: ")) for i in range(num)]
v = int(input("input the number you'd like to search for: "))
var_in_list(l, v)