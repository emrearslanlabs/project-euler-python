"""
Project Euler Problem 52

Approach:
Search positive integers in increasing order and stop at the first
number whose multiples from 2x through 6x contain exactly the same
digits as the original number.

Represent a number's digits by sorting its string representation.
Two numbers have the same digit signature if these sorted
representations are equal.

Complexity:
Time: O(n * d log d)
Space: O(d)

Where:
n = number of candidates checked
d = number of digits in each candidate

Optimization:
Search in increasing order so the first valid candidate is guaranteed
to be the smallest solution.
"""


def digit_signature(number):
    return sorted(str(number))


number = 100

while True:
    signature = digit_signature(number)

    if all(
        digit_signature(number * multiplier) == signature
        for multiplier in range(2, 7)
    ):
        break

    number += 1

print(number)