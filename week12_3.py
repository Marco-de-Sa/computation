# a function that takes a word, reverses it and then prints it
def reverse_word(word):
    temp = ""
    # a for loop that counts the indexes of the parsed word backwards and concatenates them with a temp value
    for i in range(4):
        temp = f"{temp}{word[-i-1]}"
    # takes the temp value and then prints it
    print(temp)

# a while loop that keeps looping until the input receives a word that is 4 letters long and contains the letter a
while True:
    word = input("input a word with 4 letters and an a")
    if len(word)==4 and "a" in word.lower():
        break

# calls the reverse word function
reverse_word(word)