A = 1
B = 2
C = 3

for a in range(A, 1000):
    for b in range(B, 1000):
        for c in range(C, 1000):
            if a + b + c == 1000:
                if a**2 + b**2 == c**2:
                    print(a * b * c)
                    exit()
