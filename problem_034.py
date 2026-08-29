from math import factorial

limit = 2_540_160

digit_factorials = [factorial(digit) for digit in range(10)]

total = 0
for number in range(3, limit + 1):
    curious_local_total = 0

    for digit in str(number):
        curious_local_total += digit_factorials[int(digit)]

    if curious_local_total == number:
        total += number

print(total)