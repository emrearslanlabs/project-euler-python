lower_limit = 2

upper_limit = 354_294

total = 0
for number in range(lower_limit, upper_limit + 1):
    local_total = sum(int(digits) ** 5 for digits in list(str(number)))
    if local_total == number:
        total += local_total
        

print(total)