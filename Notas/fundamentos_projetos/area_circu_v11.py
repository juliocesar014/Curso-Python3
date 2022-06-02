from math import pi
import sys


def circulo(r):
    return pi * float(r) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("É necessário informar o valor do r.")
        print("Sintaxe: {} <r>".format(sys.argv[0]))
    else:
        r = sys.argv[1]
        area = circulo(r)
        print('Area do circulo é:', area)
