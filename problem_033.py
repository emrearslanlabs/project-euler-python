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
            print(numerator, denominator)

            numerator_product *= numerator
            denominator_product *= denominator


common_divisor = gcd(
    numerator_product,
    denominator_product
)

result = denominator_product // common_divisor

print(result)