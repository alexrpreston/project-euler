def sumOfSquares(num):
    result = 0
    for i in range(1,num+1):
        result += i**2
    return result

def squareOfSums(num):
    result = 0
    for i in range(1,num+1):
        result += i
    return result**2


num = 100
difference = squareOfSums(num) - sumOfSquares(num)
print(difference)
