word, arr = input("input a word"), ["a","e","i","o","u"]
counter = 0
for i in range(len(word)):
    if word[i].lower() not in arr:
        counter += 1
print(counter)