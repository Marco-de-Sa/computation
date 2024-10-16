grade1, grade2 = float(input("input a grade between 1 and 20")), float(input("input a second grade between 1 and 20"))
print(f"{grade1}\n{grade2}")
while 1 > grade1 or grade1 > 20:
    grade1 = float(input("input a grade between 1 and 20"))

while 1 > grade2 or grade2 > 20:
    grade2 = float(input("input a second grade between 1 and 20"))

operation= input("Average for average of the grades and Greatest for greatest of the grades")

# while operation.lower() != "greatest" or operation.lower() != "average":
#     operation = input("Average for average of the grades and Greatest for greatest of the grades")

if operation.lower() == "average":
    print((grade1+grade2)/2)
elif operation.lower() == "greatest":
    print(max(grade1, grade2))