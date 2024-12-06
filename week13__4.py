def count_prime(num):
    listOfPrimes = []
    for i in range(1, num+1):
        for j in range(2, i//2+1):
            if i%j == 0:
                listOfPrimes.append(i)
                break
    return listOfPrimes

print(count_prime(int(input("gimme a number and I'll check if it a prime number: "))))