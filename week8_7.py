from random import randint

rand, guess = randint(1, 10), 11
while guess != rand:
    guess = int(input("guess the number between 1 and 10"))