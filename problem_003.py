from math import isqrt

number = 600_851_475_143

divisor = 2
largest_prime_factor = 2

if number % 2 == 0:
    while number % 2 == 0:
        number //= 2

divisor = 3


while divisor <= isqrt(number):
    if number % divisor == 0:
        while number % divisor == 0:
            number //= divisor

        largest_prime_factor = divisor

    divisor += 2

print(max(number, largest_prime_factor))