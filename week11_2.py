varType = input("insert a positive float or integer")
statement = f"{varType} is an integer"
if varType.lower() == "true" or varType.lower() == "false":
    print(f"{varType} is a boolean")
elif varType.upper() != varType.lower():
    print(f"{varType} is a string")
elif "." in varType and varType[0] == "-":
    print(f"{varType} is a negative float")
elif "." in varType:
    print(f"{varType} is a float")
elif varType[0] == "-":
    print(f"{varType} is a negative integer")
else:
    print(f"{varType} is an integer")