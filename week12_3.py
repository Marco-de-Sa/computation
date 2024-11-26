def reverse_word(word):
    temp = ""
    for i in range(4):
        temp = f"{temp}{word[-i-1]}"
    print(temp)

while True:
    word = input("input a word with 4 letters and an a")
    if len(word)==4 and "a" in word.lower():
        break

reverse_word(word)