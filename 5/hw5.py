def main():
    p = 2000000011
    q = 2000000033
    n = p * q

    divisor egcd(randrange(1, n), p - 1 * q - 1)
    while()

    divisor, x, y = egcd(p, q)
    print divisor, x, y


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

if __name__ == '__main__':
    main()
