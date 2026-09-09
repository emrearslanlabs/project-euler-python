"""
Project Euler Problem 33

Approach:
Check all two-digit fractions less than 1 and ignore trivial cases
where the numerator or denominator ends in 0.

For each fraction, find a common digit between the numerator and
denominator, remove one occurrence of that digit from both numbers,
and compare the reduced fraction with the original using
cross-multiplication.

Multiply the numerators and denominators of all valid fractions, then
reduce the final product using the Euclidean algorithm.

Complexity:
Time: O(n^2)
Space: O(1)

Optimization:
Restrict the denominator to values greater than the numerator and use
cross-multiplication instead of floating-point division.
"""


def gcd(x, y):
    while y != 0:
        x, y = y, x % y

    return x


numerator_product = 1
denominator_product = 1

for numerator in range(10, 100):
    if numerator % 10 == 0:
        continue

    for denominator in range(numerator + 1, 100):
        if denominator % 10 == 0:
            continue

        numerator_digits = list(str(numerator))
        denominator_digits = list(str(denominator))

        common_digit = None

        for digit in numerator_digits:
            if digit in denominator_digits:
                common_digit = digit
                break

        if common_digit is None:
            continue

        numerator_digits.remove(common_digit)
        denominator_digits.remove(common_digit)

        reduced_numerator = int(numerator_digits[0])
        reduced_denominator = int(denominator_digits[0])

        if reduced_denominator == 0:
            continue

        if (
            numerator * reduced_denominator
            == denominator * reduced_numerator
        ):
            numerator_product *= numerator
            denominator_product *= denominator

common_divisor = gcd(
    numerator_product,
    denominator_product
)

result = denominator_product // common_divisor

print(result)