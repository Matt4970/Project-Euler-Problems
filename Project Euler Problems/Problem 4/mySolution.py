# A palindrom number reads the same both ways. The largest palindrome made from product of two 2-digit numbers is
# 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import math

numToCheck = []
currentLargestPalindrome = 0

# Check if the number is a palindrome
def CheckPalindrome(num):
    originalArray = [i for i in str(num)]
    tempArray = originalArray
    tempArray2 = []
    for i in range(0, math.floor(len(tempArray) / 2)):
        tempArray2.append(tempArray.pop())

    # if len(originalArray) % 2 != 0:
    #     tempArray2.append(tempArray[len(tempArray) - 1])

    #print(str(num) + " is seperated into " + str(tempArray) + " == " + str(tempArray2))
    if tempArray == tempArray2:
        return num

# Nested for loops to check every combination of 3 digit numbers.
for i in range(999, 99, -1):
    for x in range(999, 99, -1):
        numToCheck = i * x
        if numToCheck > currentLargestPalindrome:
            temp = CheckPalindrome(numToCheck)
            if temp != None:
                currentLargestPalindrome = temp   

print("The largest palindrome made with two 3 digit numbers is " + str(currentLargestPalindrome))