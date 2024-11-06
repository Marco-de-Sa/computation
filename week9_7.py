grade = int(input("what is your final grade: "))
while grade < 0 or grade > 20:
    grade = int(input("please input a grade between 0 and 20: "))
if grade > 17:
    print("well done!")
else:
    print(":)")