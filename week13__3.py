def is_prime(num):
    result = False
    for i in range(2, num//2+1):
        if num%i == 0:
            result = True
            break
    return result

print(is_prime(int(input("gimme a number and I'll check if it a prime number: "))))