classes, attended, medical = int(input("how many classes do you have?: ")), int(input("how many classes did you attend?")), input("do you have a medical reason for missing the class? Y or N: ")
attendance = attended/classes
if attendance >= 0.75:
    print("you may attend the exam")
elif medical.lower() == "y" and attendance<0.75:
    print("even though you have attended less than 75% of your classes you may still attend the exam")
else:
    print("you may not attend the exam")