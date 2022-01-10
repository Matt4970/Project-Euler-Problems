# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
from os import chdir as changeDir
changeDir("Problem 8") # Change the directory so I can properly read the file

numbersArray = []
biggestProduct = 0

# Open the text file with the numers and add them into numberArray
with open("numbers.txt") as file:
    for line in file.readlines():
        for num in line:
            if num != '\n':
                numbersArray.append(num)

# Return the product of the given array
def GetProduct(numbers):
    product = int(numbers[0])
    for i in range(1,13):
        product = product * int(numbers[i])

    return product

for i in range(0, 988): # Check every number minus a few to avoid out of range error
    numberToCheck = []
    for x in range(13):
        numberToCheck.append(numbersArray[i + x]) #4702924800

    # If the product is bigger then the current largest one switch it out
    temp = GetProduct(numberToCheck)
    if biggestProduct < temp:
        biggestProduct = temp
    

print(f"The biggest product is {biggestProduct}")