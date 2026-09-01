def is_palindrome(number):
    return str(number) == str(number)[::-1]

current = 0

for first in range(1000,100,-1):
    for second in range(first,100,-1):
        if current >= first * second:
            break

        if is_palindrome(first * second):
            current = first * second

print(current)
