def get_list():
    lt = []
    for i in range(5):
        lt.append(int(input("give me a number: ")))
    return lt


def get_min(l):
    temp = l[0]
    for i in l:
        if temp > i:
            temp = i
    return temp


def can_divide(a, b):
    if a%b == 0:
        return True
    else:
        return False


print(can_divide(get_min(get_list()), 10))