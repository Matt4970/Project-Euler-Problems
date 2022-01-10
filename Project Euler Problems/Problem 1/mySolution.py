multiples = []
total = 0

for i in range(0,1000,3):
    multiples.append(i)

for i in range(0,1000,5):
    if i not in multiples:
        multiples.append(i)

for i in multiples:
    total += i

print(total)

print(multiples)