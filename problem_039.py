limit = 1_000

max_count = 0
max_p = 0

for p in range(1, limit + 1):
    local_count = 0

    for a in range(1, p // 3 + 1):
        for b in range(a + 1, (p - a + 1) // 2):
            c = p - a - b

            if a ** 2 + b ** 2 == c ** 2:
                local_count += 1

    if local_count > max_count:
        max_count = local_count
        max_p = p

print(max_p)