from math import pi


def circulo(r):
    return pi * float(r) ** 2


if __name__ == '__main__':

    r = input('Diga o valor do raio:')
    area = circulo(r)
    print('Area do circulo é:', area)
