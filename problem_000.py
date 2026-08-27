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


total = 0

for root in range(1, 488000, 2):
    total += root ** 2

print(total)