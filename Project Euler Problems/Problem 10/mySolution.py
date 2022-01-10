# Find the sums of all the primes below 2 million
import math
ceiling = 2000000
sum = 2

def CheckPrime(num):
    for i in range(3, math.ceil(num / 2), 2):
        if num % i == 0:
            return False
        
    return True

for i in range(3, ceiling + 1, 2):
    isPrime = CheckPrime(i)
    if isPrime:
        sum = sum + i

print(f"The sum of the primes below {ceiling} is {sum}")

# The correct answer is 142913828922. I got it correct after a few tweaks.