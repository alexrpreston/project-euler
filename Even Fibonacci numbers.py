firstNum = 1
secondNum = 2

fibSum = 0
while secondNum < 4000000:
    print(firstNum, secondNum)
    if secondNum%2 == 0:
        fibSum += secondNum
    temp = secondNum
    secondNum += firstNum
    firstNum = temp

print(fibSum)