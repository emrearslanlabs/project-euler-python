"""
Project Euler Problem 36

Approach:
Check only odd numbers below 1,000,000, since a binary palindrome
cannot end in 0.

For each candidate, check whether its decimal representation is a
palindrome. If it is, convert the number to binary and check whether
the binary representation is also a palindrome.

Complexity:
Time: O(n log n)
Space: O(log n)

Optimization:
The search space could be reduced further by generating decimal
palindromes directly instead of checking every odd number.
"""


def is_palindrome(value):
    return str(value) == str(value)[::-1]


total = 0

for number in range(1, 1_000_000, 2):
    if is_palindrome(number) and is_palindrome(bin(number)[2:]):
        total += number

print(total)