"""
Project Euler Problem 39

Approach:
For each perimeter p up to 1000, count the number of integer-sided
right triangles that satisfy:

a + b + c = p
a^2 + b^2 = c^2

Use a < b < c to avoid counting the same triangle multiple times.
Since c = p - a - b, only a and b need to be iterated explicitly.

Complexity:
Time: O(n^3)
Space: O(1)

Where:
n = maximum perimeter

Optimization:
Use c = p - a - b to avoid a third side loop, and restrict the ranges
of a and b using the ordering a < b < c.
"""

limit = 1_000

max_count = 0
best_perimeter = 0

for perimeter in range(1, limit + 1):
    solution_count = 0

    for a in range(1, perimeter // 3 + 1):
        for b in range(a + 1, (perimeter - a + 1) // 2):
            c = perimeter - a - b

            if a ** 2 + b ** 2 == c ** 2:
                solution_count += 1

    if solution_count > max_count:
        max_count = solution_count
        best_perimeter = perimeter

print(best_perimeter)
