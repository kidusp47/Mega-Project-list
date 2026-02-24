import math
def prime(n):
    if n < 2:
        print("Not a prime number")
        exit()
    if n == 2:
        print(2)
        exit()
    primes = [2, 3]
    for i in range(1, n):
        for j in (6*i-1,6*i+1):
            if j< 2:
                continue
            is_prime = True
            limit = int(math.sqrt(j))
            for p in primes:
                if p > limit:
                    break
                if j % p == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(j)
    print(", ".join(map(str, primes)))

num = int(input("Please enter a number: "))
prime(num)



