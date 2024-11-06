num = []
for i in range(5):
    num.append(int(input("input a number")))
for i in range(len(num)):
    if num[i] > 10:
        print(f"number: {num[i]}\nindex: {i}\n")