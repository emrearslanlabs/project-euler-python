"""
Project Euler Problem 53

Approach:
Count how many binomial coefficients nCr exceed one million
for 1 <= n <= 100.

Iterate over all valid pairs of n and r and use Python's built-in
math.comb() function to calculate each binomial coefficient.

Complexity:
Time: O(n^2)
Space: O(1)

Where:
n = maximum value of n

Note:
The time complexity treats math.comb() as a library operation.
Its internal big-integer arithmetic has additional cost.

Optimization:
Use math.comb() instead of manually recomputing factorials for every
(n, r) pair.
"""

from math import comb


n_limit = 100
threshold = 1_000_000

count = 0

for n in range(1, n_limit + 1):
    for r in range(1, n):
        if comb(n, r) > threshold:
            count += 1

print(count)