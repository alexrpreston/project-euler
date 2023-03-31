
def isNumPalindrome(num):
    strNum = str(num)
    return strNum == strNum[::-1]


num1 = 999
num2 = 999

def findThreeDigitPalindrome():
    combos = []
    for i in range(num1,1,-1):
        for j in range(num2,1,-1):
            product = i*j
            if isNumPalindrome(product):
                combos.append(product)
    return sorted(combos)

print(findThreeDigitPalindrome())