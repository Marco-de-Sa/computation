petName, pet = input("what is your pet's name?: "), input("1 if you have a dog\n2 if you cat\n3 if your pet type is not on the list\ninput:")
if "1" in pet:
    print(f"a vet visit for your dog {petName} will be {round(50*1.23, 2)} Euro")
elif "2" in pet:
    print(f"a vet visit for your cat {petName} will cost {round(40*1.23, 2)} Euro")
elif "3" in pet:
    print(f"a vet visit for you pet {petName} will cost {round(60*1.23, 2)} Euro")