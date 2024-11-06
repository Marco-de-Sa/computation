rows, column, char = int(input("how many rows would you like: ")), int(input("how many columns would you like: ")), input("what character would you like to print: ")
for i in range(rows):
    for j in range(column):
        print(char, end=" ")
    print()