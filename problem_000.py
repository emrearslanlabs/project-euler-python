"""
Project Euler Problem 0

Problem:
Find the sum of all odd square numbers among the first 488000 square numbers.

Approach:
A square number is odd if and only if its root is odd.
Instead of checking every square number, we iterate only through odd roots:

1, 3, 5, ..., 487999

For each root, calculate its square and add it to the total.

Complexity:
Time Complexity: O(n)
Space Complexity: O(1)

Optimization:
A mathematical formula could solve this in O(1),
but this iterative solution is efficient enough for the given input size
and keeps the algorithm clear.
"""


total = 0

for root in range(1, 488000, 2):
    total += root ** 2

print(total)