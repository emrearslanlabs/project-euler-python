"""
Project Euler Problem 20

Approach:
Calculate 100! iteratively by multiplying the numbers from 2 to 100.

Convert the factorial result to a string so that each digit can be
processed individually, then convert each digit back to an integer
and add it to the digit sum.

Complexity:
Time: O(n + d)
Space: O(d)

Where:
n = factorial limit
d = number of digits in n!

Optimization:
The digit sum can be written more compactly using sum() with a generator,
but the explicit loop keeps the steps clear and avoids creating an
unnecessary list of digits.
"""


limit = 100
product = 1

for factor in range(2, limit + 1):
    product *= factor

digit_sum = 0

for digit in str(product):
    digit_sum += int(digit)

print(digit_sum)