

i = num = 20

while True:
    allDivisible = True
    for j in range(1, num+1):
        if i%j != 0:
            i += num
            allDivisible = False
            break
    if allDivisible:
        break

print(i)