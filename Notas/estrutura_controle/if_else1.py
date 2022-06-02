

class cor:
    ERRO = '\033[1;31m'
    NORMAL = '\033[0;0m'


nota = float(input('Diga o valor da nota:'))


if nota > 10 or nota < 0:
    print(cor.ERRO + 'Nota invalida' + cor.NORMAL)

elif nota >= 9.1:
    print('A')


elif nota >= 8.1:
    print('A-')

elif nota >= 7.1:
    print('B')

elif nota >= 6.1:
    print('B-')

elif nota >= 5.1:
    print('C')


elif nota >= 4.1:
    print('C-')


elif nota >= 3.1:
    print('D')

elif nota >= 2.1:
    print('D-')

elif nota >= 1.1:
    print('E')

elif nota >= 0.0:
    print('E-')
else:
    print(cor.ERRO + 'Nota invalida.' + cor.NORMAL)
