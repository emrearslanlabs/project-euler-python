"""
Project Euler Problem 0

Problem:
Find the sum of all odd square numbers among the first 488000 square numbers.

Approach:
The first 488000 square numbers are:

1², 2², 3², ..., 488000²

A square number is odd if and only if its root is odd.
Therefore, instead of checking every number, we only iterate through odd roots:

1, 3, 5, ..., 487999

For each root, calculate its square and add it to the total.

Complexity:
Time Complexity: O(n)
Space Complexity: O(1)

Learning:
- "First 488000 square numbers" means the first 488000 perfect squares,
  not the square numbers less than 488000.
- Understanding the exact meaning of the problem before coding is important.
- Removing unnecessary iterations can make an algorithm cleaner.
- The input representation affects the algorithm design.

Optimization:
A mathematical formula could potentially calculate the sum in O(1),
but the iterative solution is already efficient for this problem size
and provides a clearer algorithmic approach.
"""


total = 0

for root in range(1, 488000, 2):
    total += root ** 2

print(total)