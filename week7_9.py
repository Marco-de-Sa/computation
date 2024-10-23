numChild, childList, letters, vowels = int(input("how many children would you like to have?: ")), [],0,["a","e","i","o","u"]
for i in range(numChild):
    childList.append(input(f"name of child number {i+1}: "))
for i in range(len(childList)):
    if childList[i][0].lower() in vowels:
        letters+=1
print(f"{letters} of the names start with a vowel")
