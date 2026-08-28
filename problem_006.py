"""
Project Euler Problem 6

Approach:
Calculate the sum of the squares and the sum of the numbers
from 1 to 100 in a single loop.

After the loop, square the sum of the numbers and subtract
the sum of the squares.

Complexity:
Time: O(n)
Space: O(1)

Optimization:
Can be solved in O(1) using the formulas for the sum of the first n
natural numbers and the sum of their squares.
"""


limit = 100

sum_of_squares = sum(
    number ** 2
    for number in range(1, limit + 1)
)

square_of_sum = sum(range(1, limit + 1)) ** 2

difference = square_of_sum - sum_of_squares

print(difference)