# takes a number and stores a series of operations done with that number in a dictionary
def process_num(n):
    process_dictionary = {
        "one" : f"{n ** 2}",
        "two" : f"{n**0.5}",
        "three" : f"{len(str(n))}"
    }
    return process_dictionary
# asks for a number to parse into the process_num function and parses it
number = int(input("input a num: "))
dicti = process_num(number)
# hell
print(f"{number} to the power of 2: "+dicti["one"])
print(f"square root of {number}: "+dicti["two"])
print(f"how many digits are in {number}: "+dicti["three"])