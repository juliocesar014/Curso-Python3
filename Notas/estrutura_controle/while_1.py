# while True:
#   print('Vai demorar muitoooo')

from random import randint

numero_informado = -12
numero_secreto = randint(0, 9)

while numero_informado != numero_secreto:
    numero_informado = int(input('Informe o numero:'))

print('Numero secreto {} foi encontrado!'.format(numero_secreto))
