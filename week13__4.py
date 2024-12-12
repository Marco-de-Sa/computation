def count_prime(num):
    listOfPrimes = []
    for i in range(num+1):
        for j in range(2, i // 2 + 1):
            if i % j != 0 and i % (j+1) != 0:
                listOfPrimes.append(i)
                break
            elif i%j == 0:
                break
    return listOfPrimes
print(count_prime(int(input("gimme a number and I'll cont the prime numbers between 2 and it: "))))