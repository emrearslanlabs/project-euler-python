"""
Project Euler Problem 45

Approach:
Every hexagonal number is also triangular, so only hexagonal numbers
need to be generated.

Starting after H_143, generate hexagonal numbers one by one and test
whether each value is also pentagonal.

A number x is pentagonal if:

(1 + sqrt(24x + 1)) / 6

is an integer. Use integer square root to avoid floating-point
precision issues.

Complexity:
Time: O(k)
Space: O(1)

Where:
k = number of hexagonal candidates checked

Optimization:
Skip the triangular-number check entirely because every hexagonal
number is triangular.
"""

from math import isqrt


def is_pentagonal(number):
    discriminant = 24 * number + 1
    root = isqrt(discriminant)

    return (
        root * root == discriminant
        and (1 + root) % 6 == 0
    )


def hexagonal(index):
    return index * (2 * index - 1)


index = 144

while True:
    number = hexagonal(index)

    if is_pentagonal(number):
        print(number)
        break

    index += 1