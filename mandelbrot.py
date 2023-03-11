n = " abcdefghijklmnopqrstuvwxyz"

for y in range(60):
    i = y / 60 * 4 - 2
    # i = -0.79
    row = ""
    for x in range(120):
        r = x / 120 * 4 - 2
        # r = 0.15
        # zr = x / 100 * 4 - 2
        # zi = y / 50 * 4 - 2
        zr = r
        zi = i
        r2 = r * r
        i2 = i * i
        iter = 0

        while iter < 27 and r2 + i2 < 4:
            zi = (zr + zr) * zi + i
            zr = r2 - i2 + r
            r2 = zr * zr
            i2 = zi * zi

            iter = iter + 1

        row = row + n[iter % 27]
    print(row)


