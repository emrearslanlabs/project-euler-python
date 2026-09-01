"""
Project Euler Problem 28

Approach:
Treat the spiral as a sequence of odd-sized square layers.

For each layer of size n x n, the four corner values follow a regular
pattern. Their sum can be written as:

4n^2 - 6n + 6

Start with the center value 1, then add the corner sums for all odd
layer sizes from 3 up to 1001.

Complexity:
Time: O(n)
Space: O(1)

Optimization:
The layer sums could also be combined into a closed-form expression,
reducing the time complexity to O(1), but the iterative solution is
already simple and efficient for this input size.
"""

size = 1_001
total = 1

for layer in range(3, size + 1, 2):
    total += 4 * layer * layer - 6 * layer + 6

print(total)