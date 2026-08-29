"""
Project Euler Problem 34

Approach:
Precompute the factorials of the digits from 0 to 9.

Since 1 and 2 are excluded, start the search from 10.
A seven-digit number can have a maximum digit factorial sum of 7 * 9!,
while eight-digit numbers are already too large to satisfy the condition.
Therefore, 7 * 9! is a safe upper bound.

For each candidate, sum the precomputed factorials of its digits
and check whether the result is equal to the number itself.

Complexity:
Time: O(n * d)
Space: O(d)

Where:
n = number of candidates checked
d = number of digits in each candidate

Optimization:
Precomputing the ten possible digit factorials avoids repeated
factorial calculations, and the mathematical upper bound greatly
reduces the search space.
"""


from math import factorial


digit_factorials = [factorial(digit) for digit in range(10)]

lower_bound = 10
upper_bound = 7 * digit_factorials[9]

total = 0

for number in range(lower_bound, upper_bound + 1):
    digit_factorial_sum = sum(
        digit_factorials[int(digit)]
        for digit in str(number)
    )

    if digit_factorial_sum == number:
        total += number

print(total)