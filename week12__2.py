def var_in_list(arr, var):
    positions = []
    for i in range(len(arr)):
        if arr[i] == var:
            positions.append(i)
    print(f"{var} appears in indexes {positions}")

l = [1, 2, 3, 2]
v = 2
var_in_list(l, v)