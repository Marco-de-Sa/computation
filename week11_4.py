while True:
    x = input("input: ")
    if x.isdigit() and ((x[0]!= "-" and x[0] != "0") or (x[0] != "0" and len(x) == 1)):
        break