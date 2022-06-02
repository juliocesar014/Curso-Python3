from random import randint


def sorteio_dado():
    return randint(1, 6)


for i in range(1, 7):
    if i % 2 == 1:
        continue

    if sorteio_dado() == i:
        print('Acertou o numero!!', i)
        break
else:
    print('Nao acertou o numero!!')
