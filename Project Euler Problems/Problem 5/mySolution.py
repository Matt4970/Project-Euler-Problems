# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20.

divisors = [11,12,13,14,15,16,17,18,19,20]
answer = 20
FoundNum = False

def CheckForNoRemainder(num):
    for divisor in divisors:
        if num % divisor != 0:
            return False

    return True

while FoundNum == False:
    answer += 1
    FoundNum = CheckForNoRemainder(answer)

print("The correct answer is: " + str(answer))