"""
Project Euler Problem 16

Approach:
Calculate 2^1000 directly using Python's arbitrary-precision integers.

Convert the result to a string so each digit can be processed
individually, then sum the integer value of each digit.

Complexity:
Time: O(d)
Space: O(d)

Where:
d = number of digits in 2^1000

Optimization:
A generator expression avoids creating a separate list of digits,
keeping the solution concise while reducing unnecessary memory usage.
"""


number = 2 ** 1_000
digit_sum = sum(int(digit) for digit in str(number))

print(digit_sum)