# def ask_grade():
#     try:
#         grade = int(input("what is your final grade: "))
#         while grade < 0 or grade > 20:
#             grade = int(input("please input a grade between 0 and 20: "))
#         if grade > 17:
#             temp = "well done!"
#         else:
#             temp = ":)"
#     except ValueError:
#         print("please input an integer!")
#         temp = ask_grade()
#     return temp
# print(ask_grade())

grade = input("what is your final grade: ")
while not grade.isdigit():
    grade = input("what is your final grade: ")
grade = int(grade)
while grade < 0 or grade > 20:
    grade = int(input("please input a grade between 0 and 20: "))
    if grade > 17:
        temp = "well done!"
    else:
        temp = ":)"
print(grade)