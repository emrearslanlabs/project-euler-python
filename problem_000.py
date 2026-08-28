"""
Project Euler Problem 0

Approach:
Only iterate through odd roots, since a square is odd
if and only if its root is odd.

Complexity:
Time: O(n)
Space: O(1)

Optimization:
Can be solved in O(1) using a mathematical formula
for the sum of odd squares.
"""


limit = 488_000

total = sum(root ** 2 for root in range(1, limit, 2))

print(total)