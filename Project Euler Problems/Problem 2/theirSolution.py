term_one = 1
term_two = 2

sum = 0

while(term_two <= 4000000):
    if term_two % 2 == 0:
        sum += term_two
    
    temp = term_one + term_two
    term_one = term_two
    term_two = temp

print(sum)