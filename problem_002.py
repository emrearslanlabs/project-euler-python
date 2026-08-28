"""
Project Euler Problem 2

Approach:
Generate Fibonacci numbers iteratively while keeping only the current
and next terms.

For each Fibonacci term that does not exceed 4,000,000, check whether
it is even and add it to the total if necessary.

Complexity:
Time: O(log n)
Space: O(1)

Optimization:
Every third Fibonacci number is even, so the solution could skip
the odd terms and generate only the even-valued Fibonacci numbers.
"""


current, next_number = 1, 2
total = 0

while current <= 4_000_000:
    if current % 2 == 0:
        total += current

    current, next_number = next_number, current + next_number

print(total)