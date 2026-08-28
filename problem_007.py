"""
Project Euler Problem 7

Approach:
Check prime candidates in increasing order.

Count 2 as the first prime, then test only odd numbers.
A number is prime if it has no divisor from 3 up to its square root.

Complexity:
Primality Test: O(sqrt(n))
Overall Search: O(p * sqrt(p))
Space: O(1)

Where:
p = value of the target prime

Optimization:
A sieve can generate a large number of primes more efficiently
when a suitable upper bound is known.
"""


from math import isqrt


def is_prime(number):
    if number < 2:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    for divisor in range(3, isqrt(number) + 1, 2):
        if number % divisor == 0:
            return False

    return True


target = 10_001
prime_count = 1
candidate = 3

while prime_count < target:
    if is_prime(candidate):
        prime_count += 1

        if prime_count == target:
            break

    candidate += 2

print(candidate)