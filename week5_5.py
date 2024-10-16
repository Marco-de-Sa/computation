n, p = int(input("how many sodas did you buy?")), float(input("how much did you pay for each"))
total = n*p
if total > 10:
    print("you ar spending too much on soda!!!")
else:
    print("you are within budget")
if n > 5:
    print("you are buying too many sodas!!!")