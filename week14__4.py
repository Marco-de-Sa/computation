def comparing(n, s, l):
    s1 = len(s)
    l1 = len(l)
    if n > s1 and n > l1:
        return n
    elif s1 > n and s1 > l1:
        return s
    elif l1 > n and l1 > s1:
        return l

print(comparing(int(input("give me a number!")), input("give me a string!: "), [1, 2, 3, 4, 5, 6, 7, 8]))