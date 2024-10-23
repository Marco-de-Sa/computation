dep = input("Department: ").lower()
years = int(input("Years: "))
if dep == "software" or dep == "management":
    if(years >= 3):
        print("Bonus: 30%")
    else:
        print("Bonus: 25%")
elif dep == "finance":
    if years >= 5:
        print("Bonus: 20%")
    else:
        print("Bonus: 15%")
elif dep == "maintenance":
    print("Bonus: 10%")
else:
    print("Invalid department name")