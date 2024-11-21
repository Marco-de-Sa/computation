varType = input("insert a positive float or integer")
statement = f"{varType} is an integer"

if "." in varType:
    print(f"{varType} is a float")
else:
    print(f"{varType} is an integer")