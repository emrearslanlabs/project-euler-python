"""
Project Euler Problem 9

Approach:
Iterate through possible values of a and b.
Calculate c directly from the condition a + b + c = 1000,
then check whether a^2 + b^2 = c^2.

The search ranges are reduced using the condition a < b < c.

Complexity:
Time: O(n^2)
Space: O(1)

Optimization:
The equations can be manipulated further to reduce the search
to a single loop.
"""


target_sum = 1_000

for a in range(1, target_sum // 3):
    for b in range(a + 1, (target_sum - a + 1) // 2):
        c = target_sum - a - b

        if a ** 2 + b ** 2 == c ** 2:
            product = a * b * c
            print(product)
            break