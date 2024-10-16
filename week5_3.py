n = input("Input your name")
q = bool(input("should milk be poured in before cereal? True or false?").capitalize())

if q == "True":
    print(f"{n} you are not passing comp 1")
else:
    print(f"{n} has a chance to pass")