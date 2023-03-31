



def primeFactor(num, primeSum):
    for i in range(num,2, -1):
        if num%i == 0:
            primeSum += i
            print(i)
            primeFactor(num//i, primeSum)
            
    return primeSum
        


print(primeFactor(13195, 0))