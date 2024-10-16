#declares a list
x= [1,2,3,4,5]

#prints out the first middle and last values using indexes
print(f"{x[0]}, {x[2]}, {x[4]}")
print(f"{x[-5]}, {x[-3]}, {x[-1]}")

#makes the 3rd value 43 then prints it to the console
x[2]= 42
print(x[2])

#user inputs an integer then appends it to the list which then prints it to the console
y= float(input("input an number: "))
x.append(y)
print(x)

