names = ["Anthony", "Gertrude", "Gertrudo", "Anthonella"]
for i in names:
    for j in range(len(i)):
        if i[j].lower() in "aeiou":
            print("found a vowel")