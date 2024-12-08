name = input("give me a list of names separated by a comma and a space: ")
nameList = name.split(", ")
big_font = []
small_font = []
for i in nameList:
    if 5 >= len(i):
        big_font.append(i)
    elif 5 <= len(i):
        small_font.append(i)

print(small_font)
print(big_font)