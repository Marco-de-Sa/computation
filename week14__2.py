word = input("input words separated by spaces: ")
wordList = word.split(" ")
first_letter = []
for i in wordList:
    temp = str(i)
    first_letter.append(temp[0])
print(wordList)
print(first_letter)