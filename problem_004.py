"""
Project Euler Problem 4

Approach:
Check products of three-digit numbers in descending order.

Avoid duplicate work by only testing pairs where the second factor
is less than or equal to the first. Keep track of the largest
palindrome found so far.

Because the inner loop also runs in descending order, stop checking
that row once the current product is no longer larger than the best
palindrome already found.

Complexity:
Time: O(n^2 * d)
Space: O(d)

Where:
n = number of candidate factors
d = number of digits in each product

Optimization:
Avoid symmetric duplicate pairs and break early when the remaining
products in an inner loop cannot improve the current maximum.
"""


def is_palindrome(number):
    return str(number) == str(number)[::-1]


largest_palindrome = 0

for first in range(999, 100, -1):
    for second in range(first, 100, -1):
        product = first * second

        if product <= largest_palindrome:
            break

        if is_palindrome(product):
            largest_palindrome = product

print(largest_palindrome)