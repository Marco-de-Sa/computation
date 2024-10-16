word, letter, count = input("input a word"), input("insert a letter"), 0
for i in range(len(word)):
    if word[i].lower()==letter.lower():
        count += 1
print(f"{letter} appears {count} times")