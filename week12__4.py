# takes a number and stores a series of operations done with that number in a dictionary
def process_num(n):
    process_dictionary = {
        f"{n} to the power of 2" : n**2,
        f"square root of {n}" : n**0.5,
        f"how many digits are in {n}" : len(str(n))
    }
    return process_dictionary
number = int(input("input a num: "))
print(process_num(number))