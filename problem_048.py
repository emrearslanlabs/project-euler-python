"""
Project Euler Problem 48

Approach:
Compute each term n^n modulo 10^10 and add the modular results.

Python's three-argument pow(base, exponent, modulus) performs modular
exponentiation efficiently, so the full value of n^n never needs to
be constructed.

Complexity:
Time: O(n log n)
Space: O(1)

Where:
n = number of terms in the series

Optimization:
Use modular exponentiation with pow(a, b, m) instead of computing
a^b directly and taking the modulus afterward.
"""

limit = 1_000
modulus = 10 ** 10

total = 0

for number in range(1, limit + 1):
    total = (
        total + pow(number, number, modulus)
    ) % modulus

print(total)