import math
def isPrime(num) -> bool:
    for i in range(2, int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True


primes = []
i = 2
while len(primes) < 10001:
    if isPrime(i):
        primes.append(i)
    i += 1 

print(primes)


