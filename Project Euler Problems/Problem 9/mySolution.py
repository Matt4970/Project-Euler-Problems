# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
import math
product = 0

def main():

    for a in range(1,999):
        for b in range(1,999):
            c = math.sqrt((a * a) + (b * b))
            if a + b + c == 1000:
                product = int(a * b * c)
                break

    print(f"The answer is {product}")

if __name__ == "__main__":
    main()