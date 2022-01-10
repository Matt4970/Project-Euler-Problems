import math

sumSquared = 0
sumOfSquares = 0
test = []

for i in range(1,101):
    sumSquared += i
    sumOfSquares += (i * i)

sumSquared = sumSquared * sumSquared

print(sumSquared - sumOfSquares)