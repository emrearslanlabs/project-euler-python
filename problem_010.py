"""
Project Euler Problem 10

Approach:
Use the Sieve of Eratosthenes to identify all prime numbers below
two million.

Start by marking every number from 2 onward as a prime candidate.
For each remaining prime candidate p up to sqrt(limit), mark its
multiples starting from p^2 as composite.

Finally, sum all indices that are still marked as prime.

Complexity:
Time: O(n log log n)
Space: O(n)

Optimization:
Start marking multiples from p^2 because smaller multiples have
already been eliminated by smaller prime factors.
"""

from math import isqrt


limit = 2_000_000

is_prime = [False, False] + [True] * (limit - 2)

for prime in range(2, isqrt(limit) + 1):
    if not is_prime[prime]:
        continue

    for multiple in range(prime * prime, limit, prime):
        is_prime[multiple] = False

total = sum(
    number
    for number, prime_status in enumerate(is_prime)
    if prime_status
)

print(total)