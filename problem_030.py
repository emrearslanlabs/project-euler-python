"""
Project Euler Problem 30

Approach:
Search for numbers that are equal to the sum of the fifth powers
of their digits.

For a d-digit number, the maximum possible sum of fifth powers is
d * 9^5. Seven-digit numbers are already too large to satisfy this
condition, so 6 * 9^5 provides a safe upper bound.

Precompute the fifth powers of the digits from 0 to 9, then check
each candidate within the search range.

Complexity:
Time: O(n * d)
Space: O(d)

Where:
n = number of candidates checked
d = number of digits in each candidate

Optimization:
Use the mathematical upper bound 6 * 9^5 to limit the search space,
and precompute the ten possible digit fifth powers to avoid repeated
exponentiation.
"""

digit_fifth_powers = [
    digit ** 5
    for digit in range(10)
]

lower_bound = 2
upper_bound = 6 * digit_fifth_powers[9]

total = 0

for number in range(lower_bound, upper_bound + 1):
    digit_power_sum = sum(
        digit_fifth_powers[int(digit)]
        for digit in str(number)
    )

    if digit_power_sum == number:
        total += number

print(total)