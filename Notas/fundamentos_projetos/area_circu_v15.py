from math import pi
import sys


class TerminalColor:
    ERRO = '\033[1;91m'
    NORMAL = '\033[0m'


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
        print(TerminalColor.ERRO,
              "O raio deve ser numerico!!",
              TerminalColor.NORMAL)

    else:
        r = sys.argv[1]
        area = circulo(r)
        print('Area do circulo é:', area)
