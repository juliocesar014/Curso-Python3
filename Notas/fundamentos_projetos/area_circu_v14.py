from math import pi
import sys


def help():
    print("É necessário informar o valor do r.")
    print("Sintaxe: {} <r>".format(sys.argv[0]))


def circulo(r):
    return pi * float(r) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        # sys.exit(1)

    elif not sys.argv[1].isnumeric():
        help()
        print("O raio deve ser numerico!!")
    else:
        r = sys.argv[1]
        area = circulo(r)
        print('Area do circulo é:', area)
