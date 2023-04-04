currNum = 600851475143

def isPrime(num) -> bool:
    for i in range(2,num):
        if num%i==0:
            return False
    return True


j = 2
results = []

while True:
    if j == currNum:
        results.append(j)
        break
    if currNum%j == 0 and isPrime(j):
        results.append(j)
        currNum /= j
        j = 2
    j += 1
print(results)

