term_one = 1
term_two = 2

sum = 0

fibonnachi_sequence = [1,2]

while(term_two <= 4000000):
    temp = term_one + term_two
    term_one = term_two
    term_two = temp
    fibonnachi_sequence.append(term_two)

for num in fibonnachi_sequence:
    if num % 2 == 0:
        sum += num

print(sum)