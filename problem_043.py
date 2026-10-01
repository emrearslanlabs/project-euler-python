"""
Project Euler Problem 43

Approach:
Build 0-9 pandigital numbers using backtracking.

After each new digit is added, check the corresponding
three-digit divisibility condition as soon as it becomes available.
If the condition fails, prune that branch immediately.

Complexity:
Time: O(10!) in the worst case, significantly reduced by pruning.
Space: O(10) for the recursion state.
"""

DIVISORS = [2, 3, 5, 7, 11, 13, 17]


def digits_to_number(digits):
    number = 0

    for digit in digits:
        number = number * 10 + digit

    return number


def backtrack(current_digits, used):
    if len(current_digits) == 10:
        return digits_to_number(current_digits)

    total = 0

    for digit in range(10):
        if digit in used:
            continue

        if len(current_digits) == 0 and digit == 0:
            continue

        current_digits.append(digit)
        used.add(digit)

        length = len(current_digits)
        valid = True

        if 4 <= length <= 10:
            divisor = DIVISORS[length - 4]

            value = (
                current_digits[-3] * 100
                + current_digits[-2] * 10
                + current_digits[-1]
            )

            if value % divisor != 0:
                valid = False

        if valid:
            total += backtrack(current_digits, used)

        current_digits.pop()
        used.remove(digit)

    return total


print(backtrack([], set()))