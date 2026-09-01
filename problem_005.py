"""
Project Euler Problem 5

Approach:
Compute the least common multiple of the numbers from 1 to 20
incrementally.

Use the Euclidean algorithm to calculate the greatest common divisor
of two numbers, then derive their least common multiple from the GCD.

Complexity:
Time: O(n log m)
Space: O(1)

Where:
n = number of values processed
m = magnitude of the intermediate values

Optimization:
Using the Euclidean algorithm avoids brute-force searching for a
number divisible by every value in the range.
"""


def gcd(x, y):
    while y != 0:
        x, y = y, x % y

    return x


def lcm(x, y):
    return (x // gcd(x, y)) * y


result = 1

for number in range(2, 21):
    result = lcm(result, number)

print(result)