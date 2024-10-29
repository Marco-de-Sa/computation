from random import randint

rand, guess, count = randint(1, 10), 11, 0
while guess != rand:
    guess = int(input("guess the number between 1 and 10"))
    count += 1
if count <= 2:
    print(f"congrats! you only had to guess {count} times")
elif 3 <= count <= 5:
    print(f"{count} guesses is not very impressive :(")
else:
    print("you are unlucky!")