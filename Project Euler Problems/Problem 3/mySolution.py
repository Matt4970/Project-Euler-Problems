from math import ceil

# What is the largest prime factor of 600851475143
mainNumber = 600851475143
# factors = [71, 839, 1471, 6857, 59569, 104441, 486847, 1234169, 5753023, 10086647, 87625999, 408464633, 716151937]
factors = []
nonPrimeFactors = []
# Non prime factors = 71, 839, 1471, 6857, 59569, 104441, 486847

primeFactor = 0

# Used the below code to find the factors and then I manually added it to the array up top.
for i in range(2, ceil(600851475143 / 2)):
    if mainNumber % i == 0:
        print(str(i) + ' * ' + str(mainNumber/i) + ' = ' + str(mainNumber))
        if (mainNumber/i) in factors:
            break
        factors.append(i)
        factors.append(int(mainNumber/i))

factors.sort()

for factor in factors:
    for i in range(3, ceil( factor/2 ), 2):
        print("Factor: " + str(factor) + ", i: "+ str(i) + ", Non Prime Factors: " + str(nonPrimeFactors))
        if factor % i == 0:
            nonPrimeFactors.append(factor)
            break
    
    if factor not in nonPrimeFactors:
        primeFactor = factor
        
print("The prime factor is " + str(primeFactor))