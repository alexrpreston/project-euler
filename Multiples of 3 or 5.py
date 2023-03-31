results = []
i = 0
while i < 1000:
    if i%3==0 or i%5==0:
        results.append(i)
    i += 1

print(sum(results))