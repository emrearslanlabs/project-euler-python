"""
Project Euler Problem 42

Approach:
Read the words from the provided CSV-formatted text file.

Calculate each word's value by converting its letters to their
alphabetical positions, where A = 1, B = 2, ..., Z = 26.

A number x is triangular if 8x + 1 is a perfect square.
Count the words whose values satisfy this condition.

Complexity:
Time: O(c)
Space: O(c)

Where:
c = total number of characters in the input words

Optimization:
Use integer square root to test whether 8x + 1 is a perfect square,
avoiding floating-point arithmetic and the need to generate triangle
numbers in advance.
"""

import csv
from math import isqrt


def word_value(word):
    return sum(
        ord(letter) - ord("A") + 1
        for letter in word
    )


def is_triangle(number):
    discriminant = 8 * number + 1
    root = isqrt(discriminant)

    return root * root == discriminant


with open("0042_words.txt", newline="", encoding="utf-8") as file:
    words = next(csv.reader(file))


triangle_word_count = sum(
    1
    for word in words
    if is_triangle(word_value(word))
)

print(triangle_word_count)