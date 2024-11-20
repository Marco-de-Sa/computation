from random import randint

card = [int(input("input a number between 1 and 90: ")) for i in range(3)]
bingo = [randint(1, 90) for i in range(70)]
print(bingo)
hitCount = 0
hits = [bingo[i] for i in range(len(bingo)) if bingo[i] in card]
if len(hits) >= 3:
    print(f"Threengo!{hits}")
else:
    print(f"better luck next time, the numbers you got right were {hits}")