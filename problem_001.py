"""
Project Euler Problem 1

Approach:
Check every natural number below 1000 and add it to the total
if it is divisible by 3 or 5.

Complexity:
Time: O(n)
Space: O(1)

Optimization:
Can be solved in O(1) using arithmetic series and inclusion-exclusion.
"""


total = 0

for number in range(1, 1000):
    if number % 3 == 0 or number % 5 == 0:
        total += number

print(total)