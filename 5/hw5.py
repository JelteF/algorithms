#!/usr/bin/python3

from random import randrange


def main():
    p = 101
    q = 251
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 0
    d = 0
    m = 25

    while True:
        e = randrange(2, phi_n)
        divisor, x, y = egcd(e, phi_n)

        if divisor == 1:
            d = modinv(e, phi_n)
            if d is not False:
                break

    print('message: ' + str(m))
    print('encoding key: ' + str(e))
    print('decoding key: ' + str(d))
    c = m**e % n
    print('encoded message: ' + str(c))
    dec = c**d % n
    print('decoded message: ' + str(dec))


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return False
    else:
        return x % m

if __name__ == '__main__':
    main()
