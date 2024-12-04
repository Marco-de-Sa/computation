# takes a number and stores a series of operations done with that number in a dictionary
def process_num(n):
    process_dictionary = {
        f"{n} to the power of 2: " : f"{n ** 2}",
        f"square root of {n}: " : f"{n**0.5}",
        f"how many digits are in {n}: " : f"{len(str(n))}"
    }
    return process_dictionary
# asks for a number to parse into the process_num function and parses it
number = int(input("input a num: "))
dicti = process_num(number)
# hell
print(f"{number} to the power of 2: "+dicti[f"{number} to the power of 2: "])
print(f"square root of {number}: "+dicti[f"square root of {number}: "])
print(f"how many digits are in {number}: "+dicti[f"how many digits are in {number}: "])