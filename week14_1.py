while True:
    x = input("input your username")
    if not(x.lower() == "admin" or " " in x or x.lower() == "user"):
        break
print(f"welcome {x}!")