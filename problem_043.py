"""
Project Euler Problem 43

Approach:
Build pandigital numbers using backtracking. Reject a prefix as soon as
its latest three-digit substring fails the corresponding divisibility rule.
Exclude a leading zero, then sum the completed numbers.

Complexity:
Time: O(10! * 10) in the worst case before pruning.
Space: O(k * 10) for k valid permutations, plus the recursion stack.

Optimization:
Check divisibility during construction instead of generating and testing
all permutations. Accumulate each number from left to right to preserve
its decimal place values.
"""

valid_permutations = []

divisors = [2, 3, 5, 7, 11, 13, 17]

def backtrack(current_digits, used):
    if len(current_digits) == 10:
        valid_permutations.append(current_digits.copy())
        return

    for digit in range(10):
        if digit in used:
            continue

        if len(current_digits) == 0 and digit == 0:
            continue

        current_digits.append(digit)
        used.add(digit)

        length = len(current_digits)

        if 4 <= length <= 10:
            divisor = divisors[length - 4]

            value = (
                current_digits[-3] * 100
                + current_digits[-2] * 10
                + current_digits[-1]
            )

            if value % divisor != 0:
                current_digits.pop()
                used.remove(digit)
                continue

        backtrack(current_digits, used)

        current_digits.pop()
        used.remove(digit)


backtrack([], set())

total = 0
for digits in valid_permutations:

    value = 0

    for digit in digits:
        value = value * 10 + digit

    total += value

print(total)
