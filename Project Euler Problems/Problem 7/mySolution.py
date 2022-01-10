# What is the 10001st Prime Number
import math as m

primeNumbersFound = 2
currentNumber = 4

def CheckPrime(num):
    if num % 2 == 0:
        return 0
    for i in range(3, m.ceil(num / 2), 2):
        if num % i == 0:
            return 0
    print(str(primeNumbersFound + 1) + " " + str(num))
    return 1

while primeNumbersFound != 10001:
    currentNumber += 1
    primeNumbersFound += CheckPrime(currentNumber)