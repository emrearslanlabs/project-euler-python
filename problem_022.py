"""
Project Euler Problem 22

Approach:
Read the names from the provided CSV-formatted text file and sort them
alphabetically.

For each name, calculate its alphabetical value using A = 1, B = 2,
..., Z = 26. Multiply that value by the name's 1-based position in the
sorted list, then add all name scores together.

Complexity:
Time: O(n log n + c)
Space: O(c)

Where:
n = number of names
c = total number of characters across all names

Optimization:
Sort the names in place to avoid creating an additional sorted list,
and use enumerate(..., start=1) for the problem's 1-based positions.
"""

import csv


def word_value(word):
    return sum(
        ord(letter) - ord("A") + 1
        for letter in word
    )


with open("0022_names.txt", newline="", encoding="utf-8") as file:
    names = next(csv.reader(file))

names.sort()

total = 0

for position, name in enumerate(names, start=1):
    total += position * word_value(name)

print(total)