"""
Project Euler Problem 3

Approach:
Repeatedly divide the number by its smallest possible factors.

Remove all factors of 2 first, then test only odd divisors.
Whenever a divisor is found, divide it out completely before
continuing with the next candidate.

The search stops once the divisor exceeds the square root of the
remaining number. If a value greater than 1 remains, it is the
largest remaining prime factor.

Complexity:
Time: O(sqrt(n))
Space: O(1)

Optimization:
Skip even divisors after removing all factors of 2, and update the
square-root bound using the shrinking remainder.
"""

from math import isqrt


remaining = 600_851_475_143
largest_prime_factor = 2

if remaining % 2 == 0:
    while remaining % 2 == 0:
        remaining //= 2

divisor = 3

while divisor <= isqrt(remaining):
    if remaining % divisor == 0:
        while remaining % divisor == 0:
            remaining //= divisor

        largest_prime_factor = divisor

    divisor += 2

print(max(remaining, largest_prime_factor))