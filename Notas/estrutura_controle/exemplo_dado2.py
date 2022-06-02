from random import randint

sorteio_dado = randint(1, 6)
numero = randint(1, 6)

while True:
    numero = randint(1, 6)

    if numero and sorteio_dado % 2 == 1:
        continue

    elif numero == sorteio_dado:
        print('ACERTOU.', numero, 'e', sorteio_dado)
        break
    else:
        print('Não acertou o numero.')
