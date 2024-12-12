while True:
    x = int(input("give me a number:"))
    if not(len(str(x)) <= 1 or x < 0 or x%2 != 0):
        break