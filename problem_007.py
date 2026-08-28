def is_prime(sayi):
    if sayi < 2:
        return False

    if sayi == 2:
        return True

    if sayi % 2 == 0:
        return False

    for bolen in range(3,int(sayi ** 0.5) + 1,2):
        if sayi % bolen == 0:
            return False

    return True


sayac = 0
sayi = 1

while sayac < 10001:

    if is_prime(sayi):
        sayac += 1

    if sayac == 10001:
        print(sayi)

    sayi += 1
    