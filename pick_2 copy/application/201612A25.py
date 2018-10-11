def skipped_number(k):

    if k == 1:
        print(5)
    else:
        epsilon = 0

        while (epsilon ** 2) < (10 ** k):
            epsilon = epsilon + 1

        n = 25 * 10**(k - 2) + epsilon

        print(n)

skipped_number(1)
skipped_number(2)
skipped_number(3)
skipped_number(4)
skipped_number(5)
skipped_number(6)
skipped_number(7)
skipped_number(8)
skipped_number(9)
skipped_number(10)
skipped_number(11)
skipped_number(12)
skipped_number(13)
skipped_number(14)
skipped_number(15)
skipped_number(16)
