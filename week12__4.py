def process_num(n):
    thisdict = {
        f"{n} to the power of 2" : n**2,
        f"square root of {n}" : n**0.5,
        f"how many digits are in {n}" : len(str(n))
    }
    return thisdict
    # temp = []
    # temp.append(n**2)
    # temp.append(n**0.5)
    # temp.append(len(str(n)))
    # return temp
number = int(input("input a num: "))
print(process_num(number))